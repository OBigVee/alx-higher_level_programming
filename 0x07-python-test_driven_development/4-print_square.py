#!/usr/bin/python3
"""functions print a square the `#` character"""


def print_square(size):
    """ function takes an argument size
        Args:
            size(int): the size length of the square
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and (size > 0) :
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#"*size)
    #print()
