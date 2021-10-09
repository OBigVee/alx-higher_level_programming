#!/usr/bin/python3
""" function do a matrix product of two  matrices"""


def matrix_mul(m_a, m_b):
    """ function multiply matrix
    Args:
        m_a (int):  first matrix
        m_b (int):  second matrix
    Returns:
        a new matrix 
    """
    if not m_a:
        raise TypeError("m_a must be a list")
    if not m_b:
        raise TypeError("m_b must be a list")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list of lists")
    if (m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]):
        raise ValueError("m_a can't be empty or m_b can't be empty")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        for element in row:
            if not isinstance (element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if not all(len(row) == len(m_a[0]) for row in m_a):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if not all(len(row) == len(m_b[0]) for row in m_b):
            raise TypeError("each row of m_b must be of the same size")        
   
    mat_mul = []   
    mat_a = [[col for col in row] for row in m_a]
    mat_b = [[col for col in row] for row in m_b]
    for i in range(len(mat_a)):
        for j in mat_a[i]:
            mat_a[i][j] * mat_b[i][j]
    print(mat_b)
    mat_mul = mat_a * mat_b
    return mat_mul
