#!/usr/bin/python3
""" Student class which defines a sudent by
    first_name
    last_name
    age
"""


class Student:
    """ initialisation"""
    def __init__(self, first_name, last_name, age):
        """ """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    
    def to_json(self):
        """ to_json: retrieves a dict representation of a Student instance """
        return self.__dict__
