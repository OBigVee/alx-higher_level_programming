#!/usr/bin/python3
"""
function returns the number of keys in a dict
"""


def number_keys(a_dictionary):
    keys_ = []
    for i in a_dictionary.keys():
        keys_.append(i)
    return len(keys_)
