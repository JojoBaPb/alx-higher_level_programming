#!/usr/bin/python3
def search_replace(my_list, search, replace):

    if len(my_list) == 0:
        return my_list

    new_list = [elemnt if elemnt != search else replace for elemnt in my_list]
    return new_list
