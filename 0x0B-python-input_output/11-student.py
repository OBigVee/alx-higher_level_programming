#!/usr/bin/python3
"""Student class"""


class Student:
    """class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = second_name
        self.age = age

    def to_json(self, attrs=None):
        """method retrieves a dict rep of a Student
        instance (same as 8-class_to_json.py)
        """
        if attrs is not None:
            if all(isinstance(i, str) for i in attrs):
                dict = {}
                for k, v in self.__dict__.items():
                    if k in attrs:
                        dict[k] = v
                return dict
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """method replaces all attributes of the Student instance"""
        for k, v in json.items():
            self.__dict__[k] = v
