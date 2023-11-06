#!/usr/bin/python3
"""This module contains a function that
returns True if the object is an instance
of a class that inherited (directly or indirectly)
frm the specified class ; otherwise False.
"""


def add_attribute(obj, attr_name, attr_value):
    """
    returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    if not hasattr(obj, attr_name):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
