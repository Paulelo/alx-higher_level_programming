#!/usr/bin/python3
"""A function that returns True if the object
is an instance of a class that inherited
(directly or indirectly) from the specified
class ; otherwise False."""


def inherits_from(obj, a_class):
    """A function that returns True or False

    Args:
        obj (any): object to compare
        a_class (any): object to compare against
    Return:
        True or false
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
