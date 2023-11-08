#!/usr/bin/python3
"""Module documentation
"""


def write_file(filename="", text=""):
    """Function documentation
    """
    with open(filename, 'w', encoding='utf-8') as file:
        char_count = file.write(text)
        return char_count
