#!/usr/bin/python3
"""
Calculating area and circumference
"""
import math


class MagicClass:
    """ calculating area and circumference """
    def __init__(self, radius=0):
        """ calculating area and circumference """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """ calculating area and circumference """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ calculating area and circumference """
        return 2 * math.pi * self.__radius
