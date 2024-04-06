#!/usr/bin/python3


def search_replace(my_list, search, replace):
    updated_list = my_list
    for j in range(len(updated_list)):
        if updated_list[j] == search:
            updated_list[j] = replace
    return (updated_list)
