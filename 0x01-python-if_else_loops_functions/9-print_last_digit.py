#!/usr/bin/python3
def print_last_digit(number):
    number = int(number)
    if number >= 0:
        x = number % 10
        return x
    if number < 0:
        x = number % -10
        return x
