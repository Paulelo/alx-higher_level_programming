#!/usr/bin/python3
def print_last_digit(number):
# number = int(number)
    if number >= 0:
        y = number % 10
        print('{}'.format(y), end='')
        return y
    if number < 0:
        x = (number % -10) * (-1)
        print('{}'.format(x), end='')
        return x
