#!/usr/bin/python3
"""function creates an object from JSON file """


import json



def load_from_json_file(filename):
    """ filename: """
    with open(filename, "r") as obj_file:
        return json.load(obj_file)
        
       
