#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_key = sorted(a_dictionary.keys())
        for element in dict_key:
        print("{}: {}".format(element, a_dictionary[element]))
