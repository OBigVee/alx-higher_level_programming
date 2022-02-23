#!/usr/bin/python3
"""
    script takes in a url, send a request to the url and display the of the X-Request_Id variable
"""

from urllib import response


if __name__ == "__main__":
    import urllib.request 
    import sys

    the_url = sys.argv[1]
    with urllib.request.urlopen(the_url) as response:
        output = response.info()
        print(output["X-Requested-Id"])