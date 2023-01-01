#!/usr/bin/python3
def best_score(a_dictionary):
    a_list = []
    h = 0
    if a_dictionary is None:
        return (None)
    for i in a_dictionary:
        a_list.append(int(a_dictionary[i]))
    for j in a_list:
        if j > h:
            h = j
    for k in a_dictionary:
        if h == int(a_dictionary[k]):
            biggest_key = k
    return (biggest_key)
