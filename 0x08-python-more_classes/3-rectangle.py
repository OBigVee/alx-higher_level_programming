#!/usr/bin/python3
""" defines rectangle class with instance attribute"""


class Rectangle:
    """represent Rectangle"""

    def __init__(self, width=0, height=0):
        """rectangle attributes at set to be private
        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width accesser/ getter. gets the current value of the width"""
        return self.__width

    @property
    def height(self):
        """height acesser/getter. gets the current value of the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """width mutator/setter, sets a new width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """height mutator/setter, sets a new height value for height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """method returns the rectangle area
        formula: (height * width)
        """
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of rectangle
        formula: 2(height + width)
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        string = ""
        # for i in range(self.height):
        string += "\n".join("#" * self.width for i in range(self.height))
        return string
