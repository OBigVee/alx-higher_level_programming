#!/usr/bin/python3
"""function writes a string to a text file(UTF8) and
returns the number of the characters written"""


def write_file(filename="", text=""):
    """
    Args:
        filename: name of the file to process
        text: text to be append to the file filename
    """
    with open(filename, mode="w", encoding="utf-8") as file_obj:
        data = file_obj.write(text)
        return data
