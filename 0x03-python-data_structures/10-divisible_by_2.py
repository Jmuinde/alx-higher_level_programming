#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    updated_list = []
    for k in my_list:
        if k % 2 == 0:
            updated_list.append(True)
        else:
            updated_list.append(False)
    return updated_list
