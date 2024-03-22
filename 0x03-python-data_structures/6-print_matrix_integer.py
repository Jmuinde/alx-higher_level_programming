#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        for r in m:
            print("{:d}".format(r), end="" if r == m[-1] else " ")
        print()
