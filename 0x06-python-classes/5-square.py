#!/usr/bin/python3
"""Square class defined based on '4-square.py'"""


class Square:
    """Represents a 2D polygon with 4 side equal to each other
    """
    def __init__(self, size=0):
        """ initialize Square with size

        Args:
            size (int): the size of the square.
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """Computes the area of square.

        Returns:
            int: the computed area
        """
        return self.__size ** 2

    def my_print(self):
        """ print a square based on the size given"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
