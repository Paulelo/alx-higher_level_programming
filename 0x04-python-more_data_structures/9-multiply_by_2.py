#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_list = []
    b_dictionary = dict(a_dictionary)
    for i in a_dictionary:
        a_list.append(i)
    for j in a_list:
        b_dictionary[j] = int(a_dictionary[j]) * 2
    return (b_dictionary)
