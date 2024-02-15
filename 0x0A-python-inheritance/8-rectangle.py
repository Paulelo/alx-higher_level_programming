#!/usr/bin/python3
"""A module that defines a class based on 6-base_geometry"""


class BaseGeometry:
    """A class with some functions"""
    def area(self):
        """A function that raises an exception

        Args:
            None
        Return:
            Nothing
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates an integer

        Args:
            name (str): var name of int
            value (int): int assigned to name
        Returns:
            Nothing
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer" .format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0" .format(name))


class Rectangle(BaseGeometry):
    """A class rectangle inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initiating function"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
