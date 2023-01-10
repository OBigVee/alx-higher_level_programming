#!/usr/bin/python3
"""function reads a text file(utf8) and prints it to stdout"""


def read_file(filename=""):
    """Args:
    filename: name of file to be process
    """
    with open(filename, encoding="utf-8") as file_obj:
        read_data = file_obj.read()
        print(read_data, end="")
