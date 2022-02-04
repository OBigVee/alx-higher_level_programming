#!/usr/bin/python3
"""function returns the JSON representation of an object  """

import json 

def to_json_string(my_obj):
    """ my_obj: primitive data type to be decoded to a JSON file """
    response = json.dumps(my_obj)
    return response


