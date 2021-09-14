#!/usr/bin/python3
def no_c(my_string):
    # function removes c and C from string arg
    # using list comprehension
    _string = [chr for chr in my_string if chr != "C" and chr != "c"]
    return("".join(_string))
