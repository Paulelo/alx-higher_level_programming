#!/usr/bin/python3
def islower(c):
    a = 'abcdefghijklmnopqrstuvwxyz'
    lst = list(a)
    b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lsa = list(b)
    if c in lst:
        return True
    elif c in lsa:
        return False
