#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
    Prints the items of a list in a reversed order
    Parameters:
    my_list (list): The list of integers
    '''
    if my_list is not None:
        last_idx = len(my_list) - 1
        for i in range(last_idx + 1):
            print('{:d}'.format(my_list[last_idx - i]))
