#!/usr/bin/python3
def element_at(my_list, idx):
    lent = len(my_list)
    if idx < 0:
        return (None)
    if idx > (lent - 1):
        return (None)
    element = my_list[idx]
    return (element)
