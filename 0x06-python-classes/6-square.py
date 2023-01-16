#!/usr/bin/python3
""" Write a class Square that defines a square by: (based on 5-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a
TypeError exception with the message size must be an integer
if size is less than 0, raise a
ValueError exception with the message size must be >= 0
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise raise a
TypeError exception with the message
position must be a tuple of 2 positive integers
Instantiation with optional size and optional position:
def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self):
that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
position should be use by using space -
Dont fill lines by spaces when position[1] > 0
You are not allowed to import any module """


class Square:
    """ Write a class Square that defines a square by: (based on 5-square.py)

    Attributes:
        size (:obj:`int`, optional): size of squre
        position (tuple): position to print square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Setter checks if TypeError occured
        before setting value"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Area returns the area of square

        Example:
            >>> result = Square(3)
            >>> print(result.area())
            9

        """
        return (self.__size ** 2)

    def my_print(self):
        """My_print prints square in position specified by
        the position attribute.

        Example:
            >>> result = Square(3)
            >>> result. my_print()
            ###
            ###
            ###

            >>> my_square_2 = Square(3, (1, 1))
            >>> my_square_2.my_print()
             ###
             ###
             ###

        """
        if self.size == 0:
            print()
        else:
            for i in range(0, self.size):
                print('{}'.format(' '*self.position[0]), end='')
                for j in range(0, self.size):
                    print('{}'.format('#'), end='')
                print()
