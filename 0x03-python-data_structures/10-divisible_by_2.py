#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_r = []
    for i in my_list:
        p = (i % 2 == 0)
        list_r.append(p)
    return list_r
