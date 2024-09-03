#!/usr/bin/python3
"""
Module to divide elements of a list.
"""


def matrix_divided(matrix, div):
    """
    Args:
    matrix: Is the matrix whose entries are to be divided.
    div: The divisor

    Raises:
        TypeError: When the matrix is not a list of integers or floats.
        TypeError: When each row of the matrix is not of the same size.
        TypeError: When div is not a number (integer or float)
        ZeroDivisionError: when div is zero (0).

    Returns:
        A new matrix
    """

    if not isinstance(matrix, list) or not matrix[0] or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            "of integers/floats")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                "of integers/floats")

    count_rows = []
    for row in matrix:
        count_rows.append(len(row))
    if not all(entries == count_rows[0] for entries in count_rows):
        raise TypeError("Each row of the matrix must be of the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(i / div, 2) for i in row] for row in matrix]

    return result_matrix

