#!/usr/bin/python3
"""
function replaces an element of a list at a specific posistion
"""


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return mylist
    else:
        my_list[idx] = element
        return my_list
