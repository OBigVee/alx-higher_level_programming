#!/usr/bin/python3
"""
function replaces an element in a list at a specific position without
modifying the original list
"""


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx >= 0 and idx < len(new_list):
        new_list[idx] = element
        return new_list
