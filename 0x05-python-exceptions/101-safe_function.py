#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        value = fct(*args)
    except IndexError:
        stderr.write("Exception: list index out of range\n")
        return (None)
    except ZeroDivisionError:
        stderr.write("Exception: division by zero\n")
        return (None)
    else:
        return (value)
