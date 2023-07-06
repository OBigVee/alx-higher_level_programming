#!/usr/bin/python3
"""script takes a URL and sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    r = requests.get(url)
    print(f"{r.headers.get('X-Request-Id')}")
