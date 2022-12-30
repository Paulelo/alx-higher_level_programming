#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_new_list = []
    new = 0
    for element in my_list:
        if element not in my_new_list:
            my_new_list.append(element)
    for i in range(0, len(my_new_list)):
        new = new + my_new_list[i]
    return (new)
