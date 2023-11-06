#!/usr/bin/python3
"""This module contains a function that
prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        sorted_list = sorted(self)
        print(sorted_list)
