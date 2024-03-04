#!/usr/bin/python3
"""
post email
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    value = {"email": email}
    request = requests.post(url, value)
    print(request.text)
