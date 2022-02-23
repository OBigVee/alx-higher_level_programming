#!/usr/bin/python3
"""
    script takes in a url, send a request to the url and display the of
    the X-Request_Id variable
"""
from urllib import request
import sys

if __name__ == "__main__":
    the_url = sys.argv[1]
    with request.urlopen(the_url) as resp:
        output = resp.info()
        print(output["X-Requested-Id"])
