#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by:
(based on 3-rectangle.py)
"""


class Rectangle:
    """
    A class to represent a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle with the given width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Generate a string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for i in range(self.height):
            rectangle += "#" * self.width
            if i < self.height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        Generate a string representation of the rectangle
        for eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
