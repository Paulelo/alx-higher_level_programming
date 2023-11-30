#!/usr/bin/python3

"""
   first_name str: firstname of person to be printed
   last_name str: lastname of the person to be print
   Prints: string containing first and last name of person
"""

def say_my_name(first_name, last_name=""):
    """
    function to print first and last name of someone
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    elif type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}" .format(first_name, last_name))
    
