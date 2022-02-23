#!/usr/bin/python3
"""Script takes in a URL, sends a request to the URL and displays the
body of the response """

import requests
import sys

url = sys.argv[1]
r = requests.get(url)
try:
    r.raise_for_status()
    print(r.text)
except Exception as e:
    print("Error code:{}".format(r.status_code))
