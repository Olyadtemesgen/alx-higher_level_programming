def square_matrix_map(matrix=[]):
    square = list(map(lambda a: a**2, matrix[0]))
    square2 = list(map(lambda a: a**2, matrix[1]))
    square3 = list(map(lambda a: a**2, matrix[2]))
    return [square,square2,square3]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)
