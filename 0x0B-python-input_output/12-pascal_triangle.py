#!/usr/bin/python3
"""Technical Interview preparation"""


def pascal_triangle(n):
    """
    function returns a list of lists
    of integers representing the pascal's triangle of n
    Args:
        n(int): the range of number to work with
    """
    triangle = []
    if n <= 0:
        return triangle
    if(isinstance(n, int)):
        for i in range(n):
            line = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    line.append(1)
                elif i > 0 and j > 0:
                    line.append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle.append(line)
    return triangle
