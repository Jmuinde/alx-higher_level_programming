#!/usr/bin/python3


def search_replace(my_list, search, replace):
    update_list = my_list[:]
    for j in range(len(update_list)):
        if update_list[j] == search:
            update_list[j] = replace
    return update_list
