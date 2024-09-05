#!/usr/bin/python3
"""
Module to print first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the <first_name> and <last_name>

    Args:
    first_name: The first name.
    last_name: The last name.

    Raises:
    TypeError: If either first_name or last_name is not a string.

    Prints:
    first name.
    Last name.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

