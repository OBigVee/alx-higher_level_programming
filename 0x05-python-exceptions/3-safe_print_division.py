#!/usr/bin/python3
"""
function divides 2 integers and prints the result
"""


def safe_print_division(a, b):
    try:
        result = a / b
        return("{}".format(result))
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)
