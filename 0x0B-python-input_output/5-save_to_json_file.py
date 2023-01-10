#!/usr/bin/python3
"""function writes an object to a text file, using a
    json repersentation
"""


import json
def save_to_json_file(my_obj, filename):
    """Args:
        my_obj: object to be written to text file filename
        filename: file to be written to
    """
    with open(filename, mode="w") as f_obj:
        json_file = json.dumps(my_obj)
    return json_file
