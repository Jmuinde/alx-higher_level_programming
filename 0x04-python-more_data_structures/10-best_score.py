#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    num = 0
    top = ''
    for i, j in a_dictionary.items():
        if j > num:
            num = j
            top = i
    return top
