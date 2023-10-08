#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_lists = my_list.copy()
    new_lists[idx] = element
    return new_lists
