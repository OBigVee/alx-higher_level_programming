#!/usr/bin/python3
"""Base """
class Base:
  """
  __bn_objects:(private attr)
  """
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
