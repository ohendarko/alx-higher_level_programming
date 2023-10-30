#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by:
(based on 1-rectangle.py)
"""


class Rectangle:
    """
    Rectangle class that defines a rectangle by:
    (based on 1-rectangle.py)
    """
    def __init__(self, width=0, height=0):
        """
        Class method documentation pending
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Class method documentation pending
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Class method documentation pending
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Class method documentation pending
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Class method documentation pending
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Class method documentation pending
        """
        return self.width * self.height

    def perimeter(self):
        """
        Class method documentation pending
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
