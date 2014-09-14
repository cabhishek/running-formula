from __future__ import division
from decimal import Decimal as D

def aerodynamic_drag_engery(dist, time, height, mass):

    """ Energy requried to over come aerodynamic drag = Caero * V

        where:
            Caero = (k*d*d)/n * t*2
            k  = 0.5*p*Af*Cd
                p = air density/pressure
                Af = frontal area
                Af = (0.2025*height^0.725 * mass^ 0.425)
                Cd = drag coefficient = 0.9
                n = 0.5
    """
    pass


def _air_friction(height, mass):
    """ k  = air friction =  0.5 * p * Af * Cd
        p  = air_density
        Af = frontal area = (0.2025 * height^0.725 * mass^0.425)
        Cd = drag coefficient = 0.9
        n = 0.5
    """
    pass

def _air_density_sea_level(temperature):
    """ Temperature in Celcius
        p = air_density = po * Pb * 760^-1 * 273 * (273 + T)^ -1
        po = 1.293 kg/m
        pb = 760 Torr at sea level
    """
    Po = 1.293
    Pb = 760

    air_density = Po * (Pb / 760) * (273 / (273 + temperature))

    return air_density
