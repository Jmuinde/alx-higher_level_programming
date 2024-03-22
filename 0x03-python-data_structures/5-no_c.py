#!/usr/bin/python3


def no_c(my_string):
    string = ""
    for j in my_string:
        if j != 'c' and j !=  'C':
            string += j
    return string
