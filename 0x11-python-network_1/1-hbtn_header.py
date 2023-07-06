#!/usr/bin/python3
"""python scrip takes a URL and sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]

    with urllib.request.urlopen(url) as res:
        print(f"{res.getheader('X-Request-Id')}")
