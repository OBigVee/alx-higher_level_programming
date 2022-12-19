#!/usr/bin/python3
""" function replaces all occurences of an element
by another in a new list
"""


def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    new_list = my_list.copy()
    for elem in my_list:
        if elem == search:
            get_idx = new_list.index(elem)
            new_list[get_idx] = replace
    return new_list
