#!/usr/bin/python3
""" function returns a list with all values multiplied by a number
without using any loops
"""


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda num: num * number, my_list))
