#!/usr/bin/python3
""" script fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    # html = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- contetnt: {}".format(r.text))
