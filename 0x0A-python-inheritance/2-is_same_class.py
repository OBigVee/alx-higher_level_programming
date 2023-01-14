#!/usr/bin/python3
"""function returns True if the object is exactly an instance of
    the specified class; otherwise False.
    """


def is_same_class(obj, a_class):
    """
    Args:
       obj(object of any type)
       a_class(type)
    Returns:
        True or False
    """
    if (type(obj) is not a_class):
        return False
    return True
