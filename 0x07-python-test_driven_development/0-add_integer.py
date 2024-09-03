#!/usr/bin/python3
"""
Module to get the sum of 2 integers
"""


def add_integer(a, b=98):
    """
    Get the sum of two integers a and b.

    If either a or b is float, cast them to int.

    parameters:
    a(int or float): The first parameter to be added.
    b(int or float): the second parameter to be added, default is 98.

    Returns:
        int:The sum of and b.

    Raise:
    TypeError: if either a or b is not of type int or float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    # cast to int if either is float
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
