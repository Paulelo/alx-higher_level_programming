#!/usr/bin/python3
"""Module that defines a class
   rectangle and does nothing
"""


class Rectangle:
    """Define a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() == rect_2.area():
                return rect_1
            elif rect_1.area() < rect_2.area():
                return rect_2
            else:
                return rect_1

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        return ('\n'.join([str(self.print_symbol)*self.__width]*self.__height))

    def __repr__(self):
        return "Rectangle(" + str(self.__width)\
               + "," + " " + str(self.__height) + ")"

    def __del__(self):
        print("Bye rectangle" + '.' + '.' + '.')
        Rectangle.number_of_instances -= 1
