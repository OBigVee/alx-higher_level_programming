#!/usr/bin/python3
"""python script fetches url"""

if __name__ == "__main__":
    import urllib

    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("Body response:")
        print("\t - type: {}".format(type(the_page)))
        print("\t - content: {}".format(the_page))
        print("\t - utf8 content: {}".format(the_page.decode("utf-8")))
