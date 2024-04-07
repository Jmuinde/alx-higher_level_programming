#!/usr/bin/python3


def number_keys(a_dictionary):
    list1 = []
    tot = 0
    for x, y in a_dictionary.items():
        list1.append(x)
        a = list1.count(x)
        tot += a
    return tot
