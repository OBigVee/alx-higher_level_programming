#!/usr/bin/python3
""" function returns True if the object is an instance of a class 
    that inherited (directly) or indirectly) from the specfied class;
    otherwise Flase.
"""


def inherits_from(obj, a_class):
    """Returns:
                True : if obj is an instance of a directly or indirectly
                        inherited class a_class
                False : if not
    """
    return True if issubclass(obj.__class__, a_class) and type(obj) != a_class else False 
