#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for x, y in my_dict.items():
        new_dict[x] = y * 2
    return new_dict
