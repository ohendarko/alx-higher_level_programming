#!/usr/bin/python3
"""This module contains a class
based on 5-base_geometry module
"""


class BaseGeometry:
    """
    based on 5-base_geometry module
    """
    def area(self):
        """class method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """class method
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
