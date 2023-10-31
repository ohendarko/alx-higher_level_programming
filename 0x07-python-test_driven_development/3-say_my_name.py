#!/usr/bin/python3
"""
This module contains a funtion that adds two integers
Its test is in the test directory
"""


def say_my_name(first_name, last_name=""):
    """
    This function says your name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))