#!/usr/bin/python3
""" this scrpt shows ho to prviatize an attribute """


class Square:
    """ set up class for the square"""
    def __init__(self, size):
        """ class initialization """
        self.__size = size
