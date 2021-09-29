#!/usr/bin/python3
""" Define a square class """


class Square:
    """ Represents a Square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialises new Square
        Args:
            size (int): size of side of the square
            position (tuple): 2-tuple positive integer
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """ Gets/sets the current value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                not all(isinstance(num, int) for num in value) or
                len(value) != 2 or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        """ prints the square """
        if self.__size == 0:
            print("")
            return
        for  i  in  range ( 0 , self . __size ):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print("")

    def area(self):
        """ returns current area of the square """
        return self.__size * self.__size
