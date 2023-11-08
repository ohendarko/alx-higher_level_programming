#!/usr/bin/python3
"""Module documentation
"""
import json


def load_from_json_file(filename):
    """Function documentation
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return json.load(file)
