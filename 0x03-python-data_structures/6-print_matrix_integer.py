#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
     if len(matrix) == 0:
         print('{}'.format(matrix))
     for x in range(len(matrix)):
         for y in matrix[x]:
             if y != matrix[x][len(matrix[x]) - 1]:
                 print('{}'.format(y) , end = ' ')
             else:
                 print('{}'.format(y))

