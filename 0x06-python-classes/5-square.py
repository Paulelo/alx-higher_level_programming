#!/usr/bin/python3
""" Write a class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a
TypeError exception with the message size must be an integer
if size is less than 0, raise a
ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self):
that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
You are not allowed to import any module """


class Square:
    """ Write a class Square that defines a square by: (based on 4-square.py)

    Attributes:
        size (:obj:`int`, optional): size of square.

    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Setter checks if TypeError or ValueError occured
        before setting value"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Area xreturns the area of square

        Example:
            >>> result = Square(3)
            >>> print(result.area())
            9

        """
        return (self.__size ** 2)

    def my_print(self):
        """My_print returns the area of square

        Example:
            >>> result = Square(10)
            >>> result.my_print()
            ##########
            ##########
            ##########
            ##########
            ##########
            ##########
            ##########
            ##########
            ##########
            ##########

        """
        if self.size == 0:
            print()
        else:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print('{}'.format('#'), end='')
                print()
