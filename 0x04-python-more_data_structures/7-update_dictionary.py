#!/usr/bin/python3
"""function replaces or adds key/value in a dict"""


def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return None

    if key not in a_dictionary.keys():
        a_dictionary[key] = value
    return a_dictionary
