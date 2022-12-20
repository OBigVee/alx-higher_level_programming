#!/usr/bin/python3
"""function del a key in a dic"""


def simple_delete(a_dictionary, key):
    if a_dictionary is None:
        return None
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
