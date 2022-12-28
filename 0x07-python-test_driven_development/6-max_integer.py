#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list_=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list_) == 0:
        return None
    result = list_[0]
    i = 1
    while i < len(list_):
        if list_[i] > result:
            result = list_[i]
        i += 1
    return result
