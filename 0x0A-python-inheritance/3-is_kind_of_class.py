#!/usr/bin/python3
"""function returns True if the object is and instance of, or if the object is an instance
    of a class that inherits form the specified class; otherwise Flase
"""


def is_kind_of_class_(obj, a_class):
    """Returns:
            True if obj is an isinstance of a_class
    """
    
    if isinstance(obj, a_class):
        return True 
    else:
        return False
