#!/usr/bin/python3
"""
http request error handling
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            info = response.read()
            print(info.decode("uft-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
