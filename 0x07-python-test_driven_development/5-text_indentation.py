#!/usr/bin/python3

"""
   Indenting strings
   text str: string to be indented
   prints: an indenting string
"""

def text_indentation(text):
    """
    function to indent a string
    """
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    for r in text:
        if r not in ['.', '?', ':']:
            print(r, end='')
        else:
            print(r, end='')
            print('\n')
