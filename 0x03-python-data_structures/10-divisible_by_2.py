#!/usr/bin/pythone3
def divisible_by_2(my_list=[]):
    new_list = []
    for val in my_list:
        if val % 2:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
