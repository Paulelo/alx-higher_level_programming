#!/usr/bin/python3
"""A module that prints
a square"""


def print_square(size):
    """This fuction takes only
    one arg and use it to print a square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(0, size):
            for j in range(0, size):
                print('#', end='')
            print()
