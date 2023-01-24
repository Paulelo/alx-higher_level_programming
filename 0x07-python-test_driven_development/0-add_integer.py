#!/usr/bin/python3
"""Adds two numder"""


def add_integer(a, b=98):
    """Add_integer takes two numbers
    as arguments and returns their sum"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    elif a == float("inf") or b == float("inf"):
        raise OverflowError("cannot convert float infinity to integer")
    elif a == float("NaN") or b == float("NaN"):
        raise ValueError("cannot convert float NaN to integer")
    #elif len(str(a)) > 9:
        #raise OverflowError("int is too long")
    #elif a is None and b is None:
        
    elif type(a) == float or type(b) == float:
        return int(a + b)
    else:
        return (a + b)
