#!/usr/bin/python3
""" Each module, class, and
method must contain docstring as comments."""


class Square:
    """ Each module, class, and
    method must contain docstring as comments."""
    def __init__(self, size=0, position=(0, 0)):
        """ Each module, class, and
        method must contain docstring as comments."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(crd, int) and crd >= 0 for crd in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Each module, class, and
        method must contain docstring as comments."""
        return self.__size

    @property
    def position(self):
        """ Each module, class, and
        method must contain docstring as comments."""
        return self.__position

    @size.setter
    def size(self, value):
        """ Each module, class, and
        method must contain docstring as comments."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """ Each module, class, and
        method must contain docstring as comments."""
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(crd, int) and crd >= 0 for crd in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = value

    def area(self):
        """ Each module, class, and
        method must contain docstring as comments."""
        return self.__size ** 2

    def my_print(self):
        """ Each module, class, and
        method must contain docstring as comments."""
        dimen = self.__size
        posi = self.__position
        if dimen == 0:
            print()
        else:
            for i in range(posi[1]):
                print()
            for i in range(dimen):
                print(" " * self.__position[0] + "#" * self.__size)
