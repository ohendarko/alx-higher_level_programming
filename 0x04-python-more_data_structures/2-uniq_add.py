#!/usr/bin/python3
def uniq_add(my_list=[]):
    sm = 0
    uniq_list = my_list.copy()
    for i in uniq_list:
        if uniq_list.count(i) > 1:
            uniq_list.remove(i)
    for i in range(len(uniq_list)):
        sm += uniq_list[i]
    return sm
