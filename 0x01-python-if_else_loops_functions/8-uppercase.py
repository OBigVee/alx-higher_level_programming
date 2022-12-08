#!/usr/bin/python3
"""
function prints a string in uppercase followed by a new line
"""


def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(i), end="")
    print()
