#!/usr/bin/python3
"""function appends a string at the end of the text file and
returns the number of characters added"""


def append_write(filename="", text=""):
    """Args:
        filename: name of the file to be process
        text: text to be appended to the file filename
    """
    with open(filename, mode="a", encoding="utf-8") as f_obj:
        read_data = f_obj.write(text)
        return read_data
