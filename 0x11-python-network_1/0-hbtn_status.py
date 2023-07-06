#!/usr/bin/python3
"""python script fetches url"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    the_page = response.read()
    print("Body response:")
    print("\t - type: {}".format(type(the_page)))
    print("\t - content: {}".format(the_page))
    print("\t - utf8 content: {}".format(the_page.decode("utf-8")))
