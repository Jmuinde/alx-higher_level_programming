#!/usr/bin/python3


def new_in_list(my_list, idx, new_element):
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list
    else:
        duplicate_list = my_list.copy()
        duplicate_list[idx] = new_element
        return duplicate_list
