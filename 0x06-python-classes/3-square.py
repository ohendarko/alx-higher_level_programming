#!/usr/bin/python3
""" Each module, class, and
method must contain docstring as comments."""


class Square:
    """ Each module, class, and
    method must contain docstring as comments."""
    def __init__(self, size=0):
        """ Each module, class, and
        method must contain docstring as comments."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Each module, class, and
        method must contain docstring as comments."""
        return self.__size ** 2
