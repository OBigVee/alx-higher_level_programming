#!/usr/bin/python3
"""
  writes a string to a text file(UTF8) and returns the number of characters written
  """
def write_file(filename="", text=""):
    with open(filename, mode='w') as file:
        writeText2File = file.write(text)
        return writeText2File

