#!/usr/bin/python3
""" Rectangle class inherits from Base class"""
from base import Base

class Rectangle(Base):
    """
    class information
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x  = x
        self.y = y
    

    @property
    def width(self):
        """acceser"""
        return self.__width

    @width.setter
    def width(self, value):

        """ validate the the value for rectangle 
                height is positive interger
        Args:
            value(Int): rectangle width
        """

        if type(value) != int:
            raise TypeError ("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        validate the the value for rectangle height is positive interger
        Args:
            value(Int): rectangle height
        """
        if type(value) != int:
            raise TypeError ("height must be an integer")
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
        elif value <0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """ return the area rectangle"""
        return self.__height * self.__width