#!/usr/bin/python3
"""fucntions prints a text with 2 new lines after each of these characters
   `., ?, :`
"""


def text_indentation(text):
    """ function takes in a parameter a text parameter
        Args:
            text(str):
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, "{}\n".format(char))
    splited_lines = text.splitlines()
    for idx, line in enumerate(splited_lines):
        print(line.strip(), end='' if idx == len(line) - 1 else "\n\n")
