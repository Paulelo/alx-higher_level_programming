#!/usr/bin/python3

"""
   Prints a square
   Size int: strictly an int
   Prints a square with dimensions according to the int passed
"""

def print_square(size):
    """
    Functions that print a square
    """
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(size):
        print("#" * size)
