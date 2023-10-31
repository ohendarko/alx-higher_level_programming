#!/usr/bin/python3
"""
This module contains a funtion that adds two integers
Its test is in the test directory
"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n")
    text = text.replace("?", "?\n")
    text = text.replace(":", ":\n")
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            print(line.strip())
            print()
        else:
            print(line.strip(), end="")
