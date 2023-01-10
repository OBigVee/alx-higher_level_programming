#!/usr/bin/python3
"""function returns an object(python DS) rep by a json
    string:
"""
import json


def from_json_string(my_str):
    """Args:
    my_str:json data to be converted to python
            data structure
    """
    return json.loads(my_str)
