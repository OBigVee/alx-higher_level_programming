#!/usr/bin/python3
""" function divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ function divides matrix
    Args:
        matrix (int):  list of lists of type int
        div (int):  the int divisor
    Returns:
        a new matrix 
    """
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
        for element in row:
            if not isinstance (element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("divisio by zero")
    new_list = [[round(col/div, 2) for col in row] for row in matrix ]
    return new_list
