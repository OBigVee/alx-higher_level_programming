#!/usr/bin/python3
""" Define a square class """


class Square:
    """ Represents a Square """
    def __init__(self, size):
        """ Initialises new Square
        Args:
            size (int): size of side of the square
        """
        self.size = size

    @property
    def size(self):
        """ Gets/sets the current value of size"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """ Prints a square """
        for  i  in  range ( 0 , self . __size ):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

    def area(self):
        """ returns current area of the square """
        return self.__size * self.__size
