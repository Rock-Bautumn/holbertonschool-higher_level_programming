#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in range(0, len(matrix)):
        squared_matrix.append(list(map(lambda x: x**2, matrix[row])))
    return squared_matrix
