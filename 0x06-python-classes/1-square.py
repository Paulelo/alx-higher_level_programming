#!/usr/bin/python3
""" A class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    No modules imported """


class Square:
    """ A class Square that defines a square by: (based on 0-square.py)
        Attributes:
            size (:obj:`int`, optional): size of square.
    """
    def __init__(self, size):
        self.__size = size
