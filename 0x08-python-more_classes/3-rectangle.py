#!/usr/bin/python3
"""This module defines a
   rectangle based on
   rectangle in file 1"""


class Rectangle:
    """This class defines
       defines a retangle
       returing its area
       and perimeter"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height=0):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    def area(self):
        a = self.__width
        b = self.__height
        return a * b

    def perimeter(self):
        a = self.__width
        b = self.__height
        if a == 0 or b == 0:
            return 0
        else:
            return ((a * 2) + (b * 2))

    def __print_rec(self):
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return (str())
        return (str(self.__print_rec()))
