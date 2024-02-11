#!/usr/bin/python3
"""
Your module's verbose yet thorough docstring.

Public instance method: def lookup(self): that returns sorted list
No module was imported"""

def lookup(obj):
	"""
    Returns a sorted list of attributes and methods of an object.

    Args:
        obj (object): The object whose attributes and methods are to be looked up.

    Returns:
        list: A sorted list of attribute and method names of the object.
	"""
    return sorted(dir(obj))
