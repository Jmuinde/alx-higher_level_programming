#!/usr/bin/python3


def no_c(my_string):
    string = ""
    for j in my_string:
        if j is not 'c' and j is not 'C':
            string += j
    return string
