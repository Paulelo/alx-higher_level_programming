#!/usr/bin/python3
num1 = 0
while (num1 < 10):
    num2 = 1
    while (num2 < 10):
        if (num1 != num2):
            print('{}{}, '.format(num1, num2), end='')
            num2 = num2 + 1continue
    num1 = num1 + 1
