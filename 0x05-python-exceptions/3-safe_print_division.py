#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        b = a / b
    except ZeroDivisionError:
        b
    finally:
        if b != 0:
            print("Inside result: {}".format(b))
            return (b)
        else:
            print("Inside result: {}".format(None))
            return (None)
