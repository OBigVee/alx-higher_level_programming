#!/usr/bin/python3
""" functions writes an object to a text file, using Json representation"""

import json
def save_to_json_file(my_obj, filename):
    """ 
      my_obj: primitive data type
      filename: text file name
    """
    with open (filename, "w") as file_obj:
        json_file = json.dump(file_obj)
    return json_file
      
