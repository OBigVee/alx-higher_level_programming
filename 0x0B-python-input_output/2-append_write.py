#!/usr/bin/python3
"""
    functions append a string at the end of a text file (UTF8) 
    and returns the number of char added
"""


def append_write(filename="", text=""):
    """append file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        append2File = file.write(text)
    return append2File
