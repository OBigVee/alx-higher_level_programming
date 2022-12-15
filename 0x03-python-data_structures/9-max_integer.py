#!/usr/bin/python3
def max_integer(my_list=[]):
    _max = 0 if len(my_list) == 0 else my_list[0]
    for i in my_list:
        _max = i if i >= _max else _max
    return None if len(my_list) == 0 else _max
