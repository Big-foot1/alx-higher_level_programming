#!/usr/bin/python3
"""
http url request status
"""
import requests

if __name__ == '__main__':
    url = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(url.text.__class__))
    print("\t- content: {}".format(url.text))
