#!/usr/bin/python3
"""Script takes in a URL, sends a request to the URL
and displays the body of the responses decoded in utf-8"""

import sys
from urllib import request
from urllib.error import HTTPError
if __name__ == "__main__":

    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as res:
            res.read().decode("utf-8")
    except HTTPError as e:
        print("Error code: {}".format(e.code))
