#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_of_matrix = [k[:] for k in matrix]
    for i in range(len(copy_of_matrix)):
        for j in range(len(copy_of_matrix[i])):
            copy_of_matrix[i][j] = (copy_of_matrix[i][j]) ** 2
    return (copy_of_matrix)
