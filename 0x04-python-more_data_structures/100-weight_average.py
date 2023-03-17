#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for up in my_list:
        num += up[0] * up[1]
        den += up[1]

    return (num / den)
