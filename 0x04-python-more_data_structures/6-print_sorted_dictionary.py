#!/usr/bin/python3
"""
function prints a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(key, a_dictionary[key]))
