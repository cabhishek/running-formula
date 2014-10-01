import math

def running_cost(distance, time, elevation):
    """ Cost to move forward = Ci - Ci (.5 * V / 8.33)

    where:
            V = distance/time in units meters/second
            running_cost in units watts/kg
    """

    _running_cost = _slope_cost(distance, elevation) * (1 - 0.5 * distance / (time * 8.33))

    return _running_cost

def _slope_cost(distance, elevation):
    """ Cost of running an uphill slope = C_i

        C_i = 155.4*i^5 - 30.4*i^4 - 43.3*i^3 + 46.3*i^2 + 19.5*i + 3.6

        where:
            i = slope; unitless; elevation/distance
            C_i in units watts/kg
    """
    _slope = elevation / distance

    _slope_cost_value = 155.4 * math.pow(_slope, 5) - 30.4 * math.pow(_slope, 4) - 43.3 * math.pow(
        _slope, 3) + 46.3 * math.pow(_slope, 2) + 19.5 * _slope + 3.6

    return _slope_cost_value

'''
 def mechanical_efficiency(slope):
	""" The mechanical efficiency is 0.218 when i > 0.15 and -1.062 when i < -0.15 """

	if (i => 0.15):
		mechanical_eff = 0.218
	else if (i <= -0.15):
		mechanical_eff = -1.062
	else:
		mechanical_eff = 0

	return mechanical_eff


def metabolic_efficiency(dist, time, maxvelocity):
	""" Efficiency varies linearly according to velocity, and is bound at 0.25 and 0.50 = N_v

	    N_v = 0.25 + 0.25 * (dist/time) / maxvelocity
	"""

	velocity = dist/time

	efficiency = 0.25 + 0.25 * velocity / maxvelocity

	return efficiency
'''
