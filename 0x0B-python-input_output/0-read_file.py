#!/usr/bin/python3
"""function reads a text file(utf8) and prints it to stdout"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file_obj:
        print(file_obj.read(), end="")
