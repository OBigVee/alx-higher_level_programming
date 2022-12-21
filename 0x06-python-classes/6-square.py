#!/usr/bin/python3
"""Square class defined based on '5-square.py'"""


class Square:
    """Represents a 2D polygon with 4 side equal to each other
    """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize Square with size

        Args:
            size (int): the size of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    @position.setter
    def position(self, value):
        """Update the position of the square.

        Args:
            value (tuple): The new position of this Square.
        """
        not_valid = True
        exception_mssg = "position must be a tuple of 2 postive integers"
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        not_valid = False
        if not_valid:
            raise TypeError(exception_mssg)
        else:
            self.__position = value

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
            print("{}".format("\n" * self.position[1]), end="")
            for i in range(self.__size):
                print("{}{}".format("" * self.position[0], "#" * self.size))
