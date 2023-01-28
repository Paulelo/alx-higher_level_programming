#!/usr/bin/python3
"""This module works with matrix"""


def matrix_divided(matrix, div):
    """Takes a matrix and and an int
    as argument and divides every element
    of the matrix by the int"""
    if len(matrix) != 2:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    elif type(div) not in [int, type]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return_matrix = matrix[:]
        for i in range(0, 2):
            for j in range(0, len(matrix[i])):
                if type(matrix[i][j]) not in [int, float]:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                return_matrix[i][j] = round((matrix[i][j] / div), 2)
        return (return_matrix)
