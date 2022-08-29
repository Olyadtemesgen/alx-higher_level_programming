#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for x in range(len(matrix)):
        for y in matrix[x]:
            if y != matrix[x][len(matrix[x]) - 1]:
                print('{:d}'.format(y), end=' ')
            else:
                print('{:d}'.format(y))
