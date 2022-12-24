#!/usr/bin/python3
"""function divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """matrix is divided by div

    Args:
        matrix(int): list of list of integers or floats
        div(int / float): divisor

    Returns:
        a new matrix
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(err_msg)

    if not isinstance(matrix, list):
        raise TypeError(err_msg)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err_msg)
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(err_msg)

    for row in matrix:
        if len(row) == 0:
            raise TypeError(err_msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """for row_num in range(len(matrix)):
        if len(matrix[row_num]) != len(matrix[row_num + 1]:
                raise TypeError("Each row of the matrix must have the same size")
                """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_list
