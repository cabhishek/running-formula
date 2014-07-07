from analytics.race_bins import get_bins

from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

from decimal import Decimal as D
from funcy import first
import numpy as np
import pandas as pd
import timeit


def _sum_square_error(actual, desired):
    error = 0.
    for i in range(len(desired)):
        for j in range(len(desired[i])):
            error = error + \
                ((actual[i])[j] - (desired[i])[j]) * (
                    (actual[i])[j] - (desired[i])[j])

    return error


def get_supervised_dataset(race_data, race_factors):

    race_bins = get_bins(race_data)
    race_bin_groups = pd.DataFrame.from_dict(race_bins).groupby('race_id')

    # Input, ouput
    data_set = SupervisedDataSet(6, 15)

    for race_id, race_bin in race_bin_groups:

        # Skipe bins with fewer than 10% race population
        if not np.count_nonzero(race_bin.population_pct) > 10:
            continue

        race_factor = race_factors[race_factors.race_id == race_id]

        # If race has missing factor data then skip
        if race_factor.empty:
            continue

        input_factors = [first(race_factor.high_temp) / 100.0,
                         first(race_factor.low_temp) / 100.0,
                         first(race_factor.high_humidity) / 100.0,
                         first(race_factor.low_humidity) / 100.0,
                         first(race_factor.starting_elevation) / 10000.0,
                         first(race_factor.gross_elevation_gain) / 10000.0
                         ]

        output_factors = race_bin.population_pct.tolist()

        data_set.appendLinked(input_factors, output_factors)

    return data_set


def create_feedforward_network(supervised_dataset):
    network = FeedForwardNetwork()

    inLayer = LinearLayer(6)
    hiddenLayer = SigmoidLayer(5)
    outLayer = LinearLayer(15)

    network.addInputModule(inLayer)
    network.addModule(hiddenLayer)
    network.addOutputModule(outLayer)

    in_to_hidden = FullConnection(inLayer, hiddenLayer)
    hidden_to_out = FullConnection(hiddenLayer, outLayer)

    network.addConnection(in_to_hidden)
    network.addConnection(hidden_to_out)

    # Activate network. This is very important.
    network.sortModules()

    return network


def train_network():

    start = timeit.default_timer()

    # Read data
    race_data = pd.read_csv('data/half_ironman_data_v1.csv')
    race_factors = pd.read_csv('data/half_ironman_race_factors.csv')

    # Prepare input data
    supervised_dataset = get_supervised_dataset(race_data, race_factors)

    # Create network
    network = create_feedforward_network(supervised_dataset)

    trainData, testData = supervised_dataset.splitWithProportion(0.9)

    trainer = BackpropTrainer(network, dataset=trainData)

    # Train our network
    trainer.trainEpochs(1)

    # check network accuracy
    print _sum_square_error(network.activateOnDataset(dataset=trainData), trainData['target'])
    print _sum_square_error(network.activateOnDataset(dataset=testData),  testData['target'])

    print 'Execution time =>', timeit.default_timer() - start, 'secs'


if __name__ == "__main__":
    train_network()
