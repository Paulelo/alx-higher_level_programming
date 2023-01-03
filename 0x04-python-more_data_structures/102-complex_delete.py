#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_list = []
    for i in a_dictionary:
        a_list.append(i)
    for j in range(0, len(a_list)):
        if a_dictionary[a_list[j]] == value:
            del a_dictionary[a_list[j]]
    return (a_dictionary)
