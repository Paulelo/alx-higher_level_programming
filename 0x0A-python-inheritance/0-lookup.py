#!/usr/bin/python3
"""Retruns the list of available attr"""


def lookup(obj):
    """Return a list of an object's available attributes.

    Args:
        obj (any): The object to check
    Returns:
        List
    """
    return sorted(dir(obj))
