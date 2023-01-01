#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = []
    for i in a_dictionary:
        new_list.append(i)
    new_list.sort()
    for j in new_list:
        print('{}: {}'.format(j, a_dictionary[j]))
