from funcy import first, last
import pandas as pd
import numpy as np
import math


BIN_SIZE = 15


def get_bins(race_data):
    """ Group races and create bins (time ranges) of BIN_SIZE. For each
        bin find out pct of racers in that bin and avg time of that bin.
        Also assign bin number to identify racers and their bin they fall
        into later on.
    """
    bin_data = []
    race_groups = race_data.groupby('race_id')

    for race_id, race_group in race_groups:

        top_75_percentile = race_group[
            race_group.final_time < race_group.final_time.quantile(.75)]

        # Skip races with missing data.
        if len(top_75_percentile) == 0:
            continue

        bins = pd.cut(top_75_percentile.final_time, BIN_SIZE, right=False)

        # fastest = time.strftime(
        #     '%H:%M:%S', time.gmtime(min(top_75_percentile.final_time)))
        # slowest = time.strftime(
        #     '%H:%M:%S', time.gmtime(max(top_75_percentile.final_time)))

        # print "fastest =>", fastest
        # print "slowest =>", slowest

        bin_number = 0

        for bin_key, bin_group in top_75_percentile.groupby(bins):

            bin_number += 1

            population_pct = len(bin_group) / float(len(top_75_percentile))
            bin_avg_time = bin_group.final_time.mean()

            if math.isnan(bin_avg_time):
                # Yes Ugly. Pandas bin key is a string.
                # This split gives us bin's lower/upper range time.
                lower_range = float(first(bin_key.split(',')).strip('['))
                upper_range = float(last(bin_key.split(',')).strip(')'))

                bin_avg_time = np.mean([lower_range, upper_range])

            bin_data.append({'race_id': int(race_id),
                             'bin_number': bin_number,
                             'population_pct': population_pct,
                             'bin_avg_time': bin_avg_time
                             })
    return bin_data
