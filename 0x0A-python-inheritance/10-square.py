#!/usr/bin/python3
"""This module contains a class
Square that inherits from
Rectangle (9-rectangle.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    based on 7-base_geometry module
    """
    def __init__(self, size):
        """class method
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """class method
        """
        return self.__size ** 2

    def __str__(self):
        return f"[Rectangle] {self._Square__size}/{self._Square__size}"
