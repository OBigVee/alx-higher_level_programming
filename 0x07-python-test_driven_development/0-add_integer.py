#!/usr/bin/python3
""" add_integer function sum two int values together """


def add_integer(a, b=98):
    """function takes in two parameters:
    Args:
            a (int): first value
            b (int): second value with a defualt value 98
        """
    if not isinstance(a, (int,float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) :
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    sum = a + b
    return (sum)
