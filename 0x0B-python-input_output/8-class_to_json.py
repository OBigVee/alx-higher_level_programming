#!/usr/bin/python3
""" 
    function returns the dictionary with simple data structure(list, dictionary, string, 
    int, bool) for JSON serialization of an object
"""

def class_to_json(obj):
    """ obj: an instance of a class """
    return obj.__dict__
    
