#!/usr/bin/python3
"""
fetch intranet status page
"""
import urllib.request

if __name__ == '__main__':
    req = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        body = response.read()
    print("Body response:")
    print("\t- type: {}".format(body.__class__))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
