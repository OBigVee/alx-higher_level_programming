#!/usr/bin/python3
"""function returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class; otherwise false
"""


def is_kind_of_class(obj, a_class):
    """Args:
        obj(object of type)
        a_class(type)
    """
    if not isinstance(obj, a_class):
        return False
    return True
