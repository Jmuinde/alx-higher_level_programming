#!/usr/bin/python3
"""First bit of creating the class."""


class Square:
	"""The square class."""
	def __init__(self, size=0):
		if type(size) is not int:
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = size
