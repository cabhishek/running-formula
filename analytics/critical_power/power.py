from __future__ import division

from analytics.critical_power.caero import caero
from analytics.critical_power.ckin import ckin
from analytics.critical_power.energy_cost import running_cost

def power(distance, time, angle, height, mass, temperature, elevation):
    """
        Power (W/kg) = (Ci * nV - (Ci * nV * (.5 * (V * 8.33-1)))) + Caero * V + Ckin * V
    """

    _caero = caero(distance, time, height, mass, temperature)
    _ckin = ckin(distance, time)
    _running_cost = running_cost(distance, time, elevation)

    _power = _running_cost + _caero + _ckin

    return _power
