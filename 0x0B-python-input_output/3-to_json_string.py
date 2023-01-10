#!/usr/bin/python3
"""function returns the json representation of
    an object(string)"""
import json


def to_json_string(my_obj):
    """
    Arg:
        my_obj(string)
    """
    return json.dumps(my_obj)
