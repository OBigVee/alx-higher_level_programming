#!/usr/bin/python3
""" function that adds all unique integers in a
list (only once for each integer
"""


def uniq_add(my_list=[]):
    if my_list is None:
        return None
    total = 0
    uniq_list = set(my_list)
    for elem in uniq_list:
        total += elem
    return total
