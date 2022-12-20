#!/usr/bin/python3
"""function returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    new_dict = {}
    for i, j in a_dictionary.items():
        new_dict[i] = j * 2
    return new_dict
