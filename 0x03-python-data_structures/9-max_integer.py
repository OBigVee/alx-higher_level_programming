#!/usr/bin/python3
def max_integer(my_list=[]):
    #  function that finds the biggest integer of a list.
    max = my_list[0]
    if my_list == None:
        return None
    else:
        for val in range(len(my_list)):
            if max > my_list[val]:
                max = max
            else:
                max = my_list[val]
    return max
