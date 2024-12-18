#!/usr/bin/python3
"""A script that takes ina url and an email, sends a POST request\n
to the passed url with the email as a parameter and displays the\n
the body og response (decoded in utf-8)"""

if __name__ == "__main__":
	import urllib.parse as parse
	import urllib.request as request
	from sys import argv
	url = argv[1]
	values = {'email': argv[2]}
	data = parse.urlencode(values).encode('utf-8')
	req = request.Request(url, data)
	with request.urlopen(req) as response:
		print(response.read().decode('utf-8'))
	
