#!/usr/bin/python3
"""This module works with matrix"""
def matrix_divided(matrix, div):
    if len(matrix) != 2:
        raise TypeError("matrix must be amatrix(list of lists) of integers/floats")
    elif len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of matrix must have the same size")
    elif type(div) not in [int, type]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return_matrix = matrix[:]
        for i in range(0, 2):
            for j in range(0, len(matrix[i])):
                return_matrix[i][j] = round((matrix[i][j] / div), 2)
        return (return_matrix)
