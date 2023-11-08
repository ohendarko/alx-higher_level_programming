#!/usr/bin/python3
"""Module documentation
"""


def read_file(filename=""):
    """Function documentation
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
