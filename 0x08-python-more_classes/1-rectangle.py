#!/usr/bin/python3
""" Rectangle class with instance attribute"""


class Rectangle:
    """  represent Rectangle """
    def __init__ (self, width=0, height=0):
        """ rectangle attributes at set to be private 
          Args:
          width (int): width of the rectangle
          height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """width accesser/ getter. gets the current value of the width """
        return self.__width
      
    @property
    def height(self):
        """ height acesser/getter. gets the current value of the height  """
        return self.__height
      
    @width.setter  
    def width(self,val):
        """ width mutator/setter, sets a new width value  """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val < 0 :
            raise ValueErrot("width must be >= 0")
        else:
            self.__width = val
            
    @height.setter
    def height(self,val):
        """ height mutator/setter, sets a new height value for height """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val < 0 :
            raise ValueErrot("width must be >= 0")
        else:
            self.__height = val
