#!/usr/bin/python3
"""function returns True, if the object is an instance of a class
that inherited (directly or indirectly) from the specifed class; otherwise False.
"""


def inherits_from(obj, a_class):
    """Args:
    obj(object of any type)
    a_class(type)
    """
    if not issubclass(type(obj), a_class):
        return False
    return True
