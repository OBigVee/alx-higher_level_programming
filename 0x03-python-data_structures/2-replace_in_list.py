#!/usr/bin/python3
"""
function replaces an element of a list at a specific posistion
"""


def replace_in_list(my_list, idx, element):
    if idx < len(my_list) and idx >= 0:
        my_list[idx] = element
    return my_list
