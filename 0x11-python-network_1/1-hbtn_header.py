#!/usr/bin/python3
"""
fetch X-Request-Id from http header response
"""
import urllib.request
import sys

if __name__ == '__main__':
    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        content = response.getheader('X-Request-Id')

    print(content)
