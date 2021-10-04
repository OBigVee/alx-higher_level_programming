#!/usr/bin/python3
"""Rectangle defined based on 1-rectangle.py """


class Rectangle:
    """ Rectangle class with attributes"""
    def __init__(self, width=0, height=0):
        """ initialize new rectangle
        Args: 
          width (int): size of the width
          height (int):size of the height
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
    def width(self,value):
        """ width mutator/setter, sets a new width value  """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0 :
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
            
            
    @height.setter
    def height(self,value):
        """ height mutator/setter, sets a new height value for height """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0 :
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
            
            
    def area(self):
        """ return area of the rectangle """
        return self.__width * self.__height
    
    
    def perimeter(self):
        """ returns the perimeter  of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*(self.__width + self.__height)
        
        
    def __str__(self):
        """ returns printable str representation of the rectangle"""
        string = ""
        if self.__width !=0 and self.__height != 0:
            string += "\n".join("#" * self.__width 
                                for value in range(self.__height))
            
            return string
