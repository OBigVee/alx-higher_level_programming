#!/usr/bin/python3
""" Square class inherits from the Rectangle class"""


from rectangle import Rectangle


class Square(Rectangle):
    """ Square Class info"""

    def __init__(self,size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        """ Note that a square height and width are equal"""
        self.size = size
        

    @property
    def size(self):
        """acceser"""
        return self.__size

    @size.setter
    def size(self, value):

        """validate the the value for Square
                height is positive interger
        Args:
            value(Int): Square width which is equal to it len
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__size = value
        self.__width = self.__size
        self.__height = self.__size





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
        """y-coordinate accesser """
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
        for height_cm in range(self.__height):
            for coor_x in range(self.__x):
                print(" ", end="")
            for width_cm in range(self.__width):
                print("#", end="")
            print()

       
    def __str__(self):
        return ("[{}] ({}) {}/{} - {}").format(
            self.__class__.__name__,
            self.id,
            self.__x,
            self.__y,
            self.__size,
        )
    
    def update(self, *args, **kwargs):
        """ assigns attributes """
        if args: # not empty
            for arg in range(len(args)):
                
                if arg == 0:
                    self.id = args[0]
                elif arg == 1:
                    self.__size = args[1]
                # elif arg == 2:
                #     self.__height = args[2]
                elif arg == 2:
                    self.__x = args[2]
                elif arg == 3:
                    self.__y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
        return super().update(*args, **kwargs)