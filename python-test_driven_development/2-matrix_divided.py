#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for i in matrix:
        new_matrix.append(round(i / div, 2))
    return(new_matrix)
