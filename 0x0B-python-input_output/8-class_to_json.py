#!/usr/bin/python3
"""Module documentation
"""


def class_to_json(obj):
    """Function documentation
    """
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        return obj
