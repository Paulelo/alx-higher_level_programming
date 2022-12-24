#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        if len(tuple_a) == 1:
            tuple_a = (tuple_a[0], 0)
    if len(tuple_a) > 2:
        tuple_a = (tuple_a[0], tuple_a[1])
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        if len(tuple_b) == 1:
            tuple_b = (tuple_b[0], 0)
    if len(tuple_b) > 2:
        tuple_b = (tuple_b[0], tuple_b[1])
    int1 = int(tuple_a[0])
    int2 = int(tuple_a[1])
    int3 = int(tuple_b[0])
    int4 = int(tuple_b[1])
    result1 = int1 + int3
    result2 = int2 + int4
    result = (result1, result2)
    return (result)
