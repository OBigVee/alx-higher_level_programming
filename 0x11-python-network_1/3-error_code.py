#!/usr/bin/python3
"""script takes a URL and sends a request to the URL
and display the body of the response decoded in utf-8
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(f"{response.read().decode('utf-8')}")
    except urllib.request.URLError as e:
        if hasattr(e, "code"):
            print("Error code: {}".format(e.code))
