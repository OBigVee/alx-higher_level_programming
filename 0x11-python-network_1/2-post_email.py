#!/usr/bin/python3
"""Script takes a URL and email, sends a POST
request to the passed URL with the email as parameter,
and display the body of the response in utf-8
"""

if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request

    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(f"{response.read().decode('utf-8')}")
