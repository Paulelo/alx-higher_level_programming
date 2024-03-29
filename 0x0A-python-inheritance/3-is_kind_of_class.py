#!/usr/bin/python3
"""A module that returns True if the
object is an instance of, or if the object
is an instance of a class that inherited from,
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """A function that returns True or False

    Args:
        obj (any): object to compare
        a_class (any): object to compare against
    Return:
        True or false
    """
    return isinstance(obj, a_class)
