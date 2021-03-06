#!/usr/bin/python3
""" Rectangle class inherits from Base class"""
if __name__ == "__main__":
    from models.base import Base

    class Rectangle(Base):

        """
        class information
        """

        def __init__(self, width, height, x=0, y=0, id=None):
            super().__init__(id)
            self.width = width
            self.height = height
            self.x = x
            self.y = y

        @property
        def width(self):
            """accesser"""
            self.width = self.__width
            return self.width

        @width.setter
        def width(self, value):

            """validate the the value for rectangle
                    height is positive interger
            Args:
                value(Int): rectangle width
            """

            if type(value) != int:
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")

            self.__width = value

        @property
        def height(self):
            """accesser"""
            self.height = self.__height
            return self.height

        @height.setter
        def height(self, value):
            """
            validate the the value for rectangle height is positive interger
            Args:
                value(Int): rectangle height
            """
            if type(value) != int:
                raise TypeError("height must be an integer")
            elif value <= 0:
                raise ValueError("height must be > 0")

            self.__height = value

        @property
        def x(self):
            """accesser"""
            self.x = self.__x
            return self.x

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
            """accesser"""
            self.y = self.__y
            return self.y

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
            """return the area rectangle"""
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

            # [print("#"*self.__width) for x in range(self.__height)]

        def __str__(self):
            return ("[{}] ({}) {}/{} - {}/{}").format(
                self.__class__.__name__,
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height,
            )

        def update(self, *args, **kwargs):
            """update  assigns  arguments to each attribute
            @args:
                list of arguments
            """
            if args:  # args not empty
                for i in range(len(args)):
                    if i == 0:
                        self.id = args[0]
                    elif i == 1:
                        self.__width = args[1]
                    elif i == 2:
                        self.__height = args[2]
                    elif i == 3:
                        self.__x = args[3]
                    elif i == 4:
                        self.__y = args[4]
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)

        def to_dictionary(self):
            """function returns the dictionary representation of Rectangle"""

            return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y,
            }
