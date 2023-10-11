#!/usr/bin/python3
def search_replace(my_list, search, replace):
    work_list = my_list.copy()
    for i in range(len(work_list)):
        if work_list[i] == search:
            work_list[i] = replace
    return work_list
