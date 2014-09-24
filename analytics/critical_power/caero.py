from __future__ import division

import math

def caero(dist, time, height, mass, temperature):

    """ Careo = Energy requried to over come air resistance

        where:
            Caero = (k*d*d)/(n * t*2)

                k  = 0.5*p*Af*Cd
                p  = sea level air density
                Af = frontal_area
                Cd = drag coefficient = 0.9
                n  = 0.5

            V = avg running velocity = distance/time

        Units:
            temperature in celcius
            mass in kg
            height in meters
            dist in meters
            time in secs
    """
    Cd = 0.9 # Drag coefficient
    n  = 0.5 # Efficieny

    Af = _frontal_area(height, mass)
    p  = _air_density(temperature)

    k = 0.5 * p * Af * Cd

    Caero = k * math.pow(n, -1) * math.pow(dist, 2) * math.pow(time, -2)

    return Caero

def _frontal_area(height, mass):
    """
       height in (m) and mass in (kg)
       Af = frontal area = (0.2025 * height^0.725 * mass^0.425)
    """
    frontal_area = 0.2025 * math.pow(height, 0.725) * math.pow(mass, 0.425) * 0.226

    return frontal_area

def _air_density(temperature):
    """ Temperature in Celcius
        p  = air_density = po * pb * 760^-1 * 273 * (273 + T)^ -1
        po = 1.293 kg/m
        pb = 760 Torr at sea level
    """
    po = 1.293
    pb = 760

    air_density = po * (pb / 760) * (273 / (273 + temperature))

    return air_density
