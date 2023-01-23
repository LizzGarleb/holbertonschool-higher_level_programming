#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print('')
    for i in range(len(matrix)):  # find how many row it have
        for j in range(len(matrix[i])):  # find the coloums
            if j == len(matrix[i]) - 1:  # mark the ending of the matrix
                print("{:d}".format(matrix[i][j]))
            else:  # print next to it
                print("{:d} ".format(matrix[i][j]), end="")
