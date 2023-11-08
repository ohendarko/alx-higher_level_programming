#!/usr/bin/python3
"""Module documentation
"""


def append_write(filename="", text=""):
    """Function documentation
    """
    with open(filename, 'a', encoding='utf-8') as file:
        char_count = file.write(text)
        return char_count
