#!/usr/bin/python3
def roman_to_int(roman_string):
    a_dictionary = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    lent = len(roman_string)
    a_list = []
    if roman_string is None:
        return (0)
    for i in range(0, lent):
        a_list.append(int(a_dictionary[roman_string[i]]))
    j = a_list[0]
    if len(a_list) == 2:
        k = a_list[1]
        if j < k:
            j = k - j
        else:
            j = j + k
    else:
        for k in range(1, len(a_list)):
            k = a_list[k]
            if j < k:
                j = k - j
            else:
                j = j + k
    return (j)
