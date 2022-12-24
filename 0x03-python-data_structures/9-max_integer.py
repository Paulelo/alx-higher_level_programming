#!/usr/bin/bash
def max_integer(my_list=[]):
    i = len(my_list)
    c = my_list[0]
    j = 1
    if i == 0:
        return (None)
    while j < (i - 1):
        if c < my_list[j]:
            c = my_list[j]
        j += 1
    return (c)
