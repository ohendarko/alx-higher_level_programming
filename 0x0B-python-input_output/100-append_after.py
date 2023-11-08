#!/usr/bin/python3
"""Module documentation
"""


def load_from_json_file(filename):
    """Function documentation
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
