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
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ Each module, class, and
        method must contain docstring as comments."""
        return self.__size

    @size.setter
    def size(self, value):
        """ Each module, class, and
        method must contain docstring as comments."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Each module, class, and
        method must contain docstring as comments."""
        return self.__size ** 2

    def my_print(self):
        """ Each module, class, and
        method must contain docstring as comments."""
        dimen = self.__size
        if dimen == 0:
            print()
        else:
            for i in range(dimen):
                print("#" * self.__size)
