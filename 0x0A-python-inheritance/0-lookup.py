#!/usr/bin/python3
"""
Your module's verbose yet thorough docstring.

Public instance method: def lookup(self): that returns sorted list
No module was imported"""


def lookup(obj):
	"""Return a list of an object's available attributes."""
    return sorted(dir(obj))
