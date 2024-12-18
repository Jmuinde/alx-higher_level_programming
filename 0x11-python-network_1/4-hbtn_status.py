#!/usr/bin/python3
""" Script to fetch a url using requests package.
"""
if __name__ == "__main__":

	import requests
	r = requests.get('https://alx-intranet.hbtn.io/status')
	print(f"Body response:")
	print(f"\t- type: {type(r.text)}")
	print(f"\t- content: {r.text}")
