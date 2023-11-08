#!/usr/bin/python3
"""Module documentation
"""


class Student:
    """Class documentation
    """
    def __init__(self, first_name, last_name, age):
        """Method documentation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method documentation
        """
        if attrs is None:
            return self.__dict__
        json_data = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_data[attr] = getattr(self, attr)
        return json_data

    def reload_from_json(self, json):
        """Method documentation
        """
        for key, value in json.items():
            setattr(self, key, value)
