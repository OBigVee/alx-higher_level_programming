#!/usr/bin/python3
""" define a empty class BaseGeometry based on `6-base_geometry.py`"""


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
