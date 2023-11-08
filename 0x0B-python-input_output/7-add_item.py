#!/usr/bin/python3
"""Script documentation
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_args_to_list(args):
    """Function documentation
    """
    try:
        my_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, 'add_item.json')


if __name__ == "__main__":
    add_args_to_list(sys.argv[1:])
