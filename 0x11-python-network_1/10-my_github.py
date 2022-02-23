#!/usr/bin/python3
"""Script takes github credentials (username and passwd)
and uses the Github API to display your id"""

import requests
import sys

if __name__ == "__main__":

    url = "https://api.github.com/user"
    username = sys.argv[1]
    pToken = sys.argv[2]
    values = {"username": username, "password": pToken}
    r = requests.get(url, auth=(username, pToken))
    result = r.json()
    print(result.get("id"))
