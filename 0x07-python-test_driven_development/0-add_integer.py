#!/usr/bin/python3
"""Module with function that adds"""
def add_integer(a, b=98):
    """A function that adds 2 integers."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)


#import doctest
#doctest.testfile("0-add_integer.txt")
