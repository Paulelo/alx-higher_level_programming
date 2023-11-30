#!/usr/bin/python3
"""
   matrix list: numbers to be divided
   div: number to divide matrix
   Returns: new divided list
"""

def matrix_divided(matrix, div):
    """
    function to divide matrix
    """
    for p in matrix:
        if type(p) not in [list]:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    lent = len(matrix[0])
    for z in matrix:
        for y in z:
            if type(y) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for q in matrix:
        if len(q) != lent:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    adapted_matrix = matrix
    f = 0
    n = 0
    for r in adapted_matrix:
        n = 0
        for s in r:
            adapted_matrix[f][n] = round(s / div, 2)
            n = n + 1
        f = f + 1
    return adapted_matrix

#lim = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(matrix_divided(lim, 3))
