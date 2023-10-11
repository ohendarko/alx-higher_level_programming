#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    t_wetsum = 0
    t_wet = 0
    for s, w in my_list:
        t_wetsum += s * w
        t_wet += w
    return t_wetsum / t_wet
