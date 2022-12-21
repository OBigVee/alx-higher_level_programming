#!/usr/bin/python3
"""Square class defined based on '5-square.py'"""


class Square:
    """Represents a 2D polygon with 4 side equal to each other
    """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize Square with size
        Args:
            size (int): the size of the square.
            position (tuple): The position of the square.
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
    def size(self, value):
        """Updates the size of this Square.
        Args:
            value (int): The new size of this Square.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    @position.setter
    def position(self, value):
        """Updates the position of this Square.
        Args:
            value (tuple): The new position of this Square.
        """
        not_valid = True
        exception_mssg = "position must be a tuple of 2 postive integers"
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        not_invalid = False
        if not_invalid:
            raise TypeError(exception_mssg)
        else:
            self.__position = value

    def area(self):
        """Computes the area of  Square.
        Returns:
            int: The area of  Square.
        """
        return self.size ** 2

    def my_print(self):
        """Prints a 2D table of the '#' symbol with the size of
        this square based on its position.
        """
        if self.size == 0:
            print("")
        else:
            print("{}".format("\n" * self.position[1]), end="")
            for i in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))
