#!/usr/bin/python3
"""This module prints
name of user"""


def say_my_name(first_name, last_name=""):
    """Take two argument of
    type string and raises an
    exception if mot string"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f'My name is {first_name} {last_name}')
