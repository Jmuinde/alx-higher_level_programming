#!/usr/bin/python3


class Square:
    """Set up the class to get
		the square of a number.
    """
    def __init__(self, size=0):
        """Class inizalization.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method to get the square.
        """
        return self.__size * self.__size
