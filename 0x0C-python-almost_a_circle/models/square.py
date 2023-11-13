#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """CONSTRUCTOR"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """class method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
