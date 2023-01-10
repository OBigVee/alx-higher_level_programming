#!/usr/bin/python3
"""function creates an object
    from a JSON file
"""
import json


def load_from_json_file(filename):
    """Args:
        filename: 
    """
    with open(filename, encoding="utf-8") as f_obj:
        deserialize_obj = json.load(f_obj)
    
    return deserialize_obj
