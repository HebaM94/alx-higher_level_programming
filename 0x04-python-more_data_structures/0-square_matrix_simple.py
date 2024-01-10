#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = matrix.copy()
    for i in range(len(matrix)):
        sq_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return sq_matrix
