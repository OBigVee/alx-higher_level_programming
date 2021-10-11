#!/usr/bin/python3
"""define a Recatangle tha inherits from  class BaseGeometry based on `-base_geometry.py`"""


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
