#!/usr/bin/python3
"""
This module contains a funtion that adds two integers
Its test is in the test directory
"""


def print_square(size):
    """
    This function prints a square
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)

