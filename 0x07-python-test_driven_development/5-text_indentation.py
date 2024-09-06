#!/usr/bin/python3
"""
Module to do text_indentation
"""


def text_indentation(text):
    """
    Function to print a text with two new line after the characters:
    '.', '?', ':'.

    Args:
    text (str): The input to be formatted.

    Raises:
        TypeError: If text is not of type string.

    Returns:
         A text with two new lines after the characters '.', '?', and ':'.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # list of characters  after which to add two new lines after
    list_characters = ['.', '?', ':']

    # Go through each character in the text
    output = ""
    for char in text:
        output += char
        if char in list_characters:
            output += "\n\n"

    print("{}".format(output.strip()), end="")

