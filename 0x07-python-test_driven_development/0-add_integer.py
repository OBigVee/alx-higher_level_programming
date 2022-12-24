#!/usr/bin/python3
"""function adds 2 integers"""


def add_integer(a, b=98):
    """ add 2 integers together
    
    Args:
        a(int): first integer
        b(int): second integer

    Returns:
        int: the return value. 
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    result =  a + b
    return result
