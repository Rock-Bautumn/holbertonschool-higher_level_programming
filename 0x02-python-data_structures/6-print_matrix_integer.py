#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("\n", end="")
    else:
        for x in range(len(matrix)):
            for y in range(len(matrix)):
                if y < len(matrix) - 1:
                    print("{:d}".format(matrix[x][y]), end=' ')
                else:
                    print("{:d}".format(matrix[x][y]))