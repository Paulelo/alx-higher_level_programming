#!/usr/bin/python3

def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)


#import doctest
#doctest.testfile("0-add_integer.txt")
