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
    result = True if isinstance(obj, a_class) else False
    return result
