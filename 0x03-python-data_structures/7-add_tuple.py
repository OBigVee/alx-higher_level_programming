#!/usr/bin/python3
""" function adds 2 tuples
* Returns a tuple with 2 integers:
* The first element should be the addition of the first element of each argument
* The second element should be the addition of the second 
element of each argument
* You are not allowed to import any module
* You can assume that the two tuples will only contain integers
* If a tuple is smaller than 2, use the value 0 for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers
"""


def add_tuple(tuple_a=(), tuple_b=()):
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    result = (a0 + b0, a1 + b1)
    return result
