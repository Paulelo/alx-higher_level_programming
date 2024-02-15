#!/usr/bin/python3
"""A module that returns True if the object
is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """A function that returns True or False

    Args:
        obj (any): object to compare
        a_class (any): object to compare against
    Return:
        True or false
    """
    return type(obj) is a_class
