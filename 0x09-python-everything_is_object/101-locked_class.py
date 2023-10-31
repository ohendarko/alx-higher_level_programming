#!/usr/bin/python3
"""
Documentation pending
"""


class LockedClass:
    """
    Documentation pending
    """
    def __setattr__(self, name, value):
        """
        Documentation pending
        """
        if name != "first_name":
            raise AttributeError("'LockedClass' object has "
                                 "no attribute '" + name + "'")
        super().__setattr__(name, value)
