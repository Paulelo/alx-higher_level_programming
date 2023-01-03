#!/usr/bin/python3
def weight_average(my_list=[]):
    a_list = []
    b_list = []
    if my_list is None:
        return (0)
    for i in my_list:
        a_list.append(i[0])
        b_list.append(i[1])
    len_a = len(a_list)
    len_b = len(b_list)
    a = 0
    b = 2 + 1 + 10 + 2
    for j in range(0, len_a):
        a = a + (a_list[j] * b_list[j])
    a = a / b
    return (a)
