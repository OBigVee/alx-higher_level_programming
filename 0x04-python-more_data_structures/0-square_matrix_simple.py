#!/usr/bin/python3
"""function computes the square value of all integers of a
matrix"""


def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new_mat = []
    for row in matrix:
        mat = []
        for elem in row:
            mat.append(elem * elem)
        new_mat.append(mat)
    return new_mat


"""#return [[row[i] * row[i] for row in matrix] for i in
range(len(matrix))]"""
