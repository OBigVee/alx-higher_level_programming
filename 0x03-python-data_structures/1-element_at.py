#!/usr/bin/python3
"""function retrieves an element from a list"""


def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]
