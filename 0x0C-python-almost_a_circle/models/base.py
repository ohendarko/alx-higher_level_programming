#!/usr/bin/python3
"""first class"""
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class Method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static Method"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """static Method"""
        if json_string is None or json_string == "":
            return "[]"
        return json.dumps(json_string)

    @classmethod
    def create(cls, **dictionary):
         """class Method"""
         if not dictionary:
             return cls(1)
         required_attributes = cls.__init__.__code__.co_varnames[1:]
         dummy_values = {attr: 1 for attr in required_attributes}
         dummy_values.update(dictionary)
         dummy_instance = cls(**dummy_values)
         return dummy_instance

    @classmethod
    def save_to_file(cls, list_objs):
        """class Method"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                json_string = f.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in dictionaries]
                return instances
        except FileNotFoundError:
            return []
