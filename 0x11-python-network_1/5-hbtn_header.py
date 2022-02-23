#!/usr/bin/python3
"""Script that takes in a URL, sends a request to
the URL and displays the value of the
variable x-Requested-Id in the response header"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.post(url)
    print(r.headers.get("x-Requested-id"))
