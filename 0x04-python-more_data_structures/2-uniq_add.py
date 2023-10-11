#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    uniq_list = my_list.copy()
    for i in uniq_list:
        if uniq_list.count(i) > 1:
            uniq_list.remove(i)
    return (reduce((lambda x, y: x + y), uniq_list))
