#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by:
(based on 0-rectangle.py)
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle by:
    (based on 0-rectangle.py)
    """
    def __init__(self, width=0, height=0):
        """
        instance method for new object
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        property width read-only
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        enable change to width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        property height read-only
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        enable to set encapsulate
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
