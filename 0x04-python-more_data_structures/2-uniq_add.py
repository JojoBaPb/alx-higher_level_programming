#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_l = set(my_list)
    num = 0

    for i in uniq_l:
        num += i

    return (num)
