#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    update_dict = {}
    for i, j in a_dictionary.items():
        update_dict[i] = j * 2
    return update_dict
