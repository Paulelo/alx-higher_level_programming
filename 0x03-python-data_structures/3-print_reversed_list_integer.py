#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lent = len(my_list)
    lentn = lent - 1
    if my_list is None:
        return (None)
    while lentn >= 0:
        print('{:d}'.format(my_list[lentn]))
        lentn -= 1
