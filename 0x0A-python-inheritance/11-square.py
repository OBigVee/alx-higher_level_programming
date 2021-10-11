#!/usr/bin/python3
"""define a Recatangle tha inherits from  class BaseGeometry based on `8-base_geometry.py` and 
    base on 8-rectangle.py    
"""


class BaseGeometry:
    """define a pub method area()"""
    
    def __init__(self,):
        pass
    def area(self):
        """ raise Exception mssg"""
        raise Exception("area() is not implemented")
        
    def integer_validator(self, name, value):
        """validate values"""
        if type(value) != int:
            raise TypeError(name +" must be an integer")
        if value <= 0:
          raise ValueError( name +" must be greater than 0")

        
class Rectangle(BaseGeometry):
    """ Rectangle inherits BaseGoemery and use interger_validator to validate width
         and height
    """
    
    
    def __init__(self, width, height):
        """ initialize width and height """
        self.integer_validator("width", width)
        self.integer_validator("height",height)
        self.__width = width
        self.__height = height
        
    def area (self):
        """calculate the area of the rectangle"""
        return self.__width * self.__height
        
    def __str__(self):
        """returns the  rectangle description"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

class Square(Rectangle):
    """Square inherits from Rectangle class"""
    
    
    def __init__(self,size):
        """ instantiate size"""
        self.integer_validator("size", size)
        super().__init__(size,size)
        self.__size = size
        
    def area(self):
        """ calculate area of Square"""
        return(self.__size**2)
    
    def __str__(self):
        """return, the square description"""
       return("[Square] {}/{}".format(self.__size,self.__size))  
