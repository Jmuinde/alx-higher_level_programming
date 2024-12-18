#!/usr/bin/python3
""" A script that takes ina url, sends a request to the url\n
and displays the value of the X-Request-Id variable found \n
in the header of the response"""

if __name__ == "__main__":
	import requests
	from sys import argv
	r = requests.get(argv[1])
	print(r.headers.get('X-Request-Id'))
	
