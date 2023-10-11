#!/usr/bin/python3
def uniq_add(my_list=[]):
    sm = 0
    uniq_list = list(set(my_list))
    for i in range(len(uniq_list)):
        sm += uniq_list[i]
    return sm
