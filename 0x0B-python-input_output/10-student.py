#!/usr/bin/python3
"""Student class defined a student based on 
'9-student.py' file
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method retrieves a dictionary rep of a Student instance
        (same as '8-class_to_json.py' file).

        Agrs:
            attrs: attribute to be serialize
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
