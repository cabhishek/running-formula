import unittest

from analytics.critical_power.power import power

class TestPower(unittest.TestCase):
    def setUp(self):
      self.ironman_dist = 42195.390336

    def test_power_scenario_one(self):
        time = 1200
        angle = 10
        height = 170
        mass = 80
        temp = 30

        self.assertEquals(power(self.ironman_dist, time, angle, height, mass, temp), -14417500.372763472)
