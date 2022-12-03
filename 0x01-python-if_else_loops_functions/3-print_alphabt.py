#!/usr/bin/python3
pra = list(range(97, 101))
b = list(range(102, 113))
c = list(range(114, 123))
pra = pra + b + c
for a in pra:
    print('{}'.format(chr(a)), end='')
