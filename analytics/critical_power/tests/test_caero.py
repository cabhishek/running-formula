import unittest

from analytics.critical_power.caero import caero, _air_density, _frontal_area

class TestAerodynamicDrag(unittest.TestCase):
    def setUp(self):
      self.ironman_dist = 42195.390336

    def test_air_density_when_temp_is_20(self):
        temperature = 20

        self.assertEquals(_air_density(temperature), 1.204740614334471)

    def test_air_density_when_temp_is_60(self):
        temperature = 60

        self.assertEquals(_air_density(temperature), 1.060027027027027)

    def test_frontal_area_for_mass_70_height_170(self):
        mass = 70
        height = 170

        self.assertAlmostEquals(_frontal_area(height, mass), 51.011390570021234)

    def test_caero_scenario_one(self):
        time = 2324
        heigth = 170
        mass = 80
        temperature = 30

        self.assertEquals(caero(self.ironman_dist, time, heigth, mass, temperature), 18660.899027839263)
