#!/usr/bin/python3
"""function returns the list of available attributes and methods
    of an object
"""


def lookup(obj):
    """Args:
    obj: object whose attributes and method to be return

    Returns:
        list []
    """
    return [attr for attr in dir(obj)]
