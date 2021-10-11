#!/usr/bin/python3
"""function returns True if the object is exaclty an instance of the specified class"""


def is_same_class(obj, a_class):
    """ is_same_class accepts two argument
      Args:
        obj(object of any type)
        a_class(type)
     Returns: True of False
    """
    return (True if type(obj) == a_class else False)
