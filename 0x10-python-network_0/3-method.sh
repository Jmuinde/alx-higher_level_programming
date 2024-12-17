#!/usr/bin/bash
# Takes  in a URL,displays all the HTTP methods the server will accept. 

curl -Is "$1" | grep "Allow" | cut -d ' ' -f 2-
