import unittest

from analytics.critical_power.ckin import ckin

class TestAerodynamicDrag(unittest.TestCase):
    def setUp(self):
      self.ironman_dist = 42195.390336

    def test_ckin_scenario_one(self):
        time = 1200

        self.assertEquals(ckin(self.ironman_dist, time), 0.058604708799999995)
