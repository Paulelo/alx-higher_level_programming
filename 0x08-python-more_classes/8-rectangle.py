#!/usr/bin/python3
"""This module defines a
   rectangle based on
   rectangle in file 1"""


class Rectangle:
    """This class defines
       defines a retangle
       returing its area
       and perimeter"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = self.print_symbol

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_1.print_symbol != "#":
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif rect_2.print_symbol != "#":
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() > rect_2.area():
            return (rect_1)
        elif rect_2.area() > rect_1.area():
            return (rect_2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ('')
        return ('\n'.join([f'{self.print_symbol}' * self.width] * self.height))

    def __repr__(self):
        return (f'Rectangle({self.width}, {self.height})')

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
