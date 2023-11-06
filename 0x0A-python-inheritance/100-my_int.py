#!/usr/bin/python3
"""This module contains a class
Square that inherits from
Rectangle (9-rectangle.py).
"""


class MyInt(int):
    """
    based on something
    """
    def __eq__(self, other):
        """class method
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """class method
        """
        return super().__eq__(other)
