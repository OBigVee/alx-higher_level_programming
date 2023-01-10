#!/usr/bin/python3
"""function writes an object to a text file, using a
    json repersentation
"""
import json

def save_to_json_file(my_obj, filename):
    """Args:
        my_obj: object to be written to text file filenamere
        filename: file to be written to
    """
    with open(filename, mode="w", encoding="utf-8") as f_obj:
        json.dump(my_obj, f_obj)
        #f_obj.write(JSONEncoder().encode(my_obj))
    
