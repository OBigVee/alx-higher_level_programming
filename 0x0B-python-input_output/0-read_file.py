#! /usr/bin/python3
"""
    function that reads a text file UTF-8
    """


def read_file(filename=""):
    """Args: filename """
    with open(filename, mode='r') as file:
        read_line = file.read()
        print (read_line, end="")
