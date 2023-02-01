#!/usr/bin/python3
""" A module that prints
in style"""


def text_indentation(text):
    """ This function prints
    2 new lines after '.','?'
    and ':'."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(0, len(text)):
        print(text[i], end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print()
            print()
