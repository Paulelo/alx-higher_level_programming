#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lent = len(my_list)
    lentn = lent - 1
    while lentn >= 0:
        print('{}'.format(my_list[lentn]))
        lentn -= 1
