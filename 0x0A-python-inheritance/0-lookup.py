#!/usr/bin/python3
"""function returns a list of available attributes and methods of an object"""


def lookup(obj):
    """lookup fucntion takes an argument 
    
      Args:
          obj(object):
      Returns: list of available attributes
      """
    return dir(obj)
