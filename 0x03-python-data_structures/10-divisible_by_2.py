#!/usr/bin/pythone3
def divisible_by_2(my_list=[]):
    new_list = []
    for val in my_list:
        if val % 2 == 0:
            new_list.append(True)
            return new_list
        else:
            new_list.append(False)
        return new_list
