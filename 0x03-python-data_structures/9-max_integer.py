#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    i = len(my_list)
    c = my_list[0]
    j = 1
    while j < (i):
        if c < my_list[j]:
            c = my_list[j]
        j += 1
    return (c)
