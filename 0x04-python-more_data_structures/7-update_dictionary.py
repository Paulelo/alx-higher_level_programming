#!/usr/bin/pyhton3
def update_dictionary(a_dictionary, key, value):
    new_list = []
    for i in a_dictionary:
        new_list.append(i)
    if key in new_list:
        a_dictionary[key] = value
    else:
        a_dictionary.update({key: value, })
    return (a_dictionary)
