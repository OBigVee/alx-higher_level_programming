#!/usr/bin/python3
""" function prints a text with 2 new lines after each characters
.,? and :
"""


def text_indentation(text):
    """ print a text with 2 new lines
    after each of any of the following characters
    ., ?, :
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    special_char = [".", "?", ":"]
    for char in special_char:
        #if char in special_char:
        text = text.replace(char, "{}\n".format(char))
    split_lin = text.splitlines()
    for idx, line in enumerate(split_lin):
        print(line.strip(), end="" if idx == len(line) - 1 else "\n\n")
