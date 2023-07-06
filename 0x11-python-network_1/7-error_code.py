#!/usr/bin/python3
"""script takes in a URL, sends a
request to the URL and displays the body 
of the response."""

if __name__ == "__main__":
    import requests, sys

    url = sys.argv[1]

    r = requests.get(url)
    try:
        r.status_code == 200
        print(r.text)
    except Exception as e:
        print(f"Error code: {r.status_code}")
