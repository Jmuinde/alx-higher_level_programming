#!/usr/bin/python3
""" A script that takes ina url, sends a request to the url\n
and displays the value of the X-Request-Id variable found \n
in the header of the response"""

if __name__ == "__main__":
	import urllib.request
	from sys import argv
	req = urllib.request.Request(argv[1])
	with urllib.request.urlopen(req) as response:
		print(response.headers.get('X-Request-Id'))
	
