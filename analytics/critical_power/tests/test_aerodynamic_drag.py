import unittest

from analytics.critical_power.aerodynamic_drag import _air_density_sea_level

class TestAerodynamicDrag(unittest.TestCase):
    def setUp(self):
        pass

    def test_air_density_when_temp_is_20(self):
        temperature = 20

        self.assertEquals(_air_density_sea_level(temperature), 1.204740614334471)

    def test_air_density_when_temp_is_60(self):
        temperature = 60

        self.assertEquals(_air_density_sea_level(temperature), 1.060027027027027)
