#!/usr/bin/python3
"""python script fetches url"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as r:
    html = r.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('utf-8')))