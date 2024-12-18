#!/usr/bin/python3
"""A script that takes ina url and an email, sends a POST request\n
to the passed url with the email as a parameter"""

if __name__ == "__main__":
	import requests
	from sys import argv
	url = argv[1]
	data = {'email': argv[2]}
	r = requests.post(url, data = data)
	print(r.text)
	
