#!/usr/bin/python3
"""Base """

import json


class Base:
    """
    __bn_objects:(private attr)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """parse data to JSON"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """parse and write JSON files to list_objs overwrite if file exists
        list_objs: list of instances that inherits of Base
        """

        Fname = cls.__name__ + ".json"  # fileName
        list_text = []
        if list_objs is not None:
            for content in list_objs:
                list_text.append(content.to_dictionary())
        with open(Fname, mode="w", encoding="utf-8") as file:
            return file.write(Base.to_json_string(list_text))
