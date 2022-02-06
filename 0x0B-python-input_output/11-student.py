#!/usr/bin/python3
""" Student class which defines a sudent by
    based on (10-student.py)
"""


class Student:
    """initialisation"""

    def __init__(self, first_name, last_name, age):
        """ """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json: retrieves a dict representation of a Student
        instance (same as 8-class_to_json.py)"""
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            dict = {}
            for key, pair in self.__dict__.items():
                if key in attrs:
                    dict[key] = pair
            return dict
        else:
            return self.__dict__
    def reload_from_json(self, json):
        """ replaces all the Student instance which mimick's the reloading of data from json """
        for (key, pair) in json.items():
            setattr(self, key, pair)
