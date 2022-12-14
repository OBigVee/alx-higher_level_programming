#!/usr/bin/python3
"""
function prints all integer of a list, in reverse order
"""


def print_reversed_list_integer(my_list=[]):
    n_arr = len(my_list)
    for i in range(1, n_arr + 1):
        print(my_list[-i])
