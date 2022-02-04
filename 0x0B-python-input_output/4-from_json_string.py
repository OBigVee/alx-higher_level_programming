#!/usr/bin/python3
""" function returns an object (data type) rep by a JSON string"""

import json
def from_json_string(my_str):
    """ my_str: JSON string  """
    response = json.loads(my_str)
    return response
