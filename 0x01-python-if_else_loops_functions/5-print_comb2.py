#!/usr/bin/python3

for a in range(0, 99):
    z = a // 10
    x = a % 10
    print('{}{}'.format(z, x), end=', ')
print('99')
