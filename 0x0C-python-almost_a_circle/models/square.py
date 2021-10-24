#!/usr/bin/python3
""" Square class inherits from the Rectangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class info"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        """ Note that a square height and width are equal"""
        self.width = size
        self.height = size
        self.x = x
        self.y = y

    @property
    def width(self):
        """acceser"""
        return self.__width

    @width.setter
    def width(self, value):

        """validate the the value for rectangle
                height is positive interger
        Args:
            value(Int): Square width
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        validate the the value for Square height is positive interger
        Args:
            value(Int): Square height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """
        validate the the value for x is non negative interger
        Args:
            value(Int): x value
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ """
        return self.__y

    @y.setter
    def y(self, value):
        """
        validate the the value for y is non negative interger
        Args:
            value(Int): y value
        """

        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area Square"""
        return self.__height * self.__width

    def display(self):

        for coor_y in range(self.__y):
            print()
        for h_cm in range(self.__height):
            for coor_x in range(self.__x):
                print(" ", end="")
            for w_cm in range(self.__width):
                print("#", end="")
            print()

       
    def __str__(self):
        return ("[{}] ({}) {}/{} - {}/{}").format(
            self.__class__.__name__,
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height,
        )
