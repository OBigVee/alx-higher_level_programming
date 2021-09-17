#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    _matrix = []
    for i in matrix:
        result = list(map(lambda x: x**2, i))
        _matrix.append(result)
    return _matrix
