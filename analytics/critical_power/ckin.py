import math

def ckin(distance, time):
    """
        Ckin = Enery required to change kinetic energy

        ckin = 0.5 * n^-1 * d * t^-2

        Where
            n = 0.25
            d = distance in meters
            t = total time in secs
    """
    n = 0.25

    return 0.5 * math.pow(n, -1) * math.pow(distance, 2) * math.pow(time, -3)

