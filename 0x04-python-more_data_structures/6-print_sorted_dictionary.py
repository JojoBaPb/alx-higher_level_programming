#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ordr = list(a_dictionary.keys())
    list_ordr.sort()
    for i in list_ordr:
        print("{}: {}".format(i, a_dictionary.get(i)))
