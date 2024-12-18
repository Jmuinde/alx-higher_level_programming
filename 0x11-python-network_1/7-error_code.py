#!/usr/bin/python3
"""A script that takes in a ur, sends a request\n
to the passed url with and displays the body of response"""

if __name__ == "__main__":
	import requests
	from sys import argv
	url = argv[1]
	req = requests.get(url)
	if req.status_code >= 400:
		print(f"Error code: {req.status_code}")
	else:
		print(req.text)
