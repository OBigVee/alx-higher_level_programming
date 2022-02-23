#!/usr/bin/python3
""" script takes in a URL and Email, send a Post request
    to the passed URL with the email as a parameter, and 
    display the body of the response(decoded in `utf-8`)
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email" : sys.argv[2]}

    data = parse.urlencode(value)
    data = data.encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as resp:
        output = resp.read().decode('utf-8')