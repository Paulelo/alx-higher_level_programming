#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
    except:
        stderr.write("Exception: Unknown format code 'd' for object of type 'str'\n")
        return (False)
    else:
        if isinstance(value, str):
            return(False)
        return (True)
