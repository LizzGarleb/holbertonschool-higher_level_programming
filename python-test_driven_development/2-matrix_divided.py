#!/usr/bin/python3
def matrix_divided(matrix, div):
    msg_error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(msg_error)

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        for value in row:
            if type(value) not in [int, float]:
                raise TypeError(msg_error)

    first_row = len(matrix[0])
    for row in matrix:
        if first_row != len(row):
            raise TypeError('Each row of the matrix must have the same size')

    return [[round(i / div, 2) for i in row] for row in matrix]
