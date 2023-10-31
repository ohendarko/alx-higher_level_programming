#!/usr/bin/python3
"""
This module contains a funtion
that adds two integers
Its test is in the test directory
"""
def add_integer(a, b=98):
    """
    function that adds integers
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
