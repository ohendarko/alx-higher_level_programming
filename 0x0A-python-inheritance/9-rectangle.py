#!/usr/bin/python3
"""This module contains a class
Rectangle that inherits from
BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    based on 7-base_geometry module
    """
    def __init__(self, width, height):
        """class method
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """class method
        """
        return self.__width * self.__height

    def __str__(self):
        """class method
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
