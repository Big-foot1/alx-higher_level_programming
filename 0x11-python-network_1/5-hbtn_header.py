#!/usr/bin/python3
"""
print X-request-id from http request
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    request = requests.get(url)
    print(request.headers.get('X-Request-Id'))
