#!/usr/bin/python3
"""
    This module has a function that divides all of the items in a matrix

    Examples:
    >>> matrix_divided([[0.33, 0.77, 1.0], [1.33, 1.67, 2.0]], 3)
    [[0.11, 0.26, 0.33], [0.44, 0.56, 0.67]]
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    This function divides the items in the matrix by div
    Examples:
    >>> matrix_divided([[0.33, 0.77, 1.0], [1.33, 1.67, 2.0]], 3)
    [[0.11, 0.26, 0.33], [0.44, 0.56, 0.67]]
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    columns = len(matrix[0])
    div_matrix = []

    for row in matrix:
        if len(row) != columns:
            raise TypeError("Each row of the matrix must have the same size")
        div_row = []
        for colItem in row:
            if type(colItem) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix \
(list of lists) of integers/floats")
            div_item = round(colItem / div, 2)
            div_row.append(div_item)
        div_matrix.append(div_row)
    return div_matrix
