#!/usr/bin/python3
"""Module documentation
"""
import json


def save_to_json_file(my_obj, filename):
    """Function documentation
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
