#!/usr/bin/python3
"""function prints a square with the character #"""


def print_square(size):
    """function takes 1 argument
    Args:
        size(int): size length of square

    Returns:
        prints a square the character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TyperError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
