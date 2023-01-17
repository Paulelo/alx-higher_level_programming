#!/usr/bin/python3
"""Adds two numder"""


def add_integer(a, b=98):
    """Add_integer takes two numbers
    as arguments and returns their sum"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    elif type(a) == float or type(b) == float:
        return int(a + b)
    else:
        return (a + b)
