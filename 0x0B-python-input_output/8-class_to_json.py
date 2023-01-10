#!/usr/bin/python3

def class_to_json(obj):
    """ function returns the dict description with simple
    data structure(list, dictionary, string,integer and boolean)
    for JSON serialization of an object.

    Args:
        obj: 
    """
    return(obj.__dict__)

