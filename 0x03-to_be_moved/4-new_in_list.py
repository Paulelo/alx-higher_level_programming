#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n_my_list = my_list
    lent = len(n_my_list)
    if idx < 0:
        return (n_my_list)
    if idx > (lent - 1):
        return (n_my_list)
    n_my_list[idx] = element
    return (5)
