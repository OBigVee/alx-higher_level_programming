#!/usr/bin/python3
"""Square class defined based on '1-square.py'"""


class Square:
    """Represents a 2D polygon with 4 side equal to each other
    """
    def __init__(self, size=0):
        """ initialize Square with size

        Args:
            size (int): the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

