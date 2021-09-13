import math
from math import pi


def circle_area(radius):
    return pi * radius ** 2


def sphere_volume(radius):
    return 4.0 / 3.0 * pi * radius ** 3


def triangle_area(base, height):
    return (base * height) / 2


def friut_val(fruit):
    if fruit == 'banana':
        return 10
    elif fruit == 'apple':
        return 2
    elif len(fruit) < 6:
        return 4
    else:
        return 1



