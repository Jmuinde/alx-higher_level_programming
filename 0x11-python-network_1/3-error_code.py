#!/usr/bin/python3
"""A script that takes in a ur, sends a request\n
to the passed url with and displays the body of response (decoded in utf-8)"""

if __name__ == "__main__":
	import urllib.parse as parse
	import urllib.request as request
	import urllib.error as error
	from sys import argv
	url = argv[1]
	req = request.Request(url)
	try:
		with request.urlopen(req) as response:
			print(response.read().decode('utf-8'))
	except error.HTTPError as e:
		print(f"Error code: {e.code}")
