#!/usr/bin/python3
"""Module that defines a class
   rectangle and does nothing
"""


class Rectangle:
    """Define a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return ('\n'.join(['#' * self.__width] * self.__height))
