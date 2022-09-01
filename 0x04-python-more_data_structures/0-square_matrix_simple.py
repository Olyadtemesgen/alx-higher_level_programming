def square_matrix_simple(matrix=[]):
    new = [[row[x] * row[x] for x in range(len(row))] for row in matrix]
    return new