#!/usr/bin/python3
""" functions writes an object to a text file, using Json representation"""


def save_to_json_file(my_obj, filename):
    """ 
      my_obj: primitive data type
      filename: text file name
    """
    with open (filename, "w") as file_obj:
        file = file_obj.write(my_obj)
    return file
      
