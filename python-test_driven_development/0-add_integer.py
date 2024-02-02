#!/usr/bin/pyhton3
"""
Functions that adds two integers.
a and b must be integers or floats, otherwise raise a TypeError exception 
a and b must be first casted to integers if they are float
"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance (a, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
