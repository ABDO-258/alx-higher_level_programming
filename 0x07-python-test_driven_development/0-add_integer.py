#!/usr/bin/python3
"""
    add two value integers and floats
        @a: integers or float
        @a: integers or float
"""


def add_integer(a, b=98):
    """
    add two value integers and floats
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
