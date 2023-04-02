#!/usr/bin/python3

"""This a simple module
   that does somtin fantastic"""


class LockedClass:
    """This class does not
    accept any instance name
    that is not found in the
    slots list"""
    __slots__ = ['first_name']
