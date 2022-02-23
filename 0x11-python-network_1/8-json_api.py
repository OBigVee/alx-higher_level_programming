#!/usr/bin/python3
""" script takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user 
with the letter as a parameter."""


import requests 
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user" 
    if len(sys.argv) == 1:
        letter = {'q':""}
    else:
        letter = {"q": sys.argv[1]}
    r = requests.post(url, data=letter)
    r.json()
    try:
        if r:
            print("[{}] {}".format(r["id",r["name"]]))
        else:
            print("No Result")
    except:
        print("Not a valid JSON")


