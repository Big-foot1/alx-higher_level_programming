#!/usr/bin/python3

"""
takes your GitHub credentials (username and password)
and uses
the GitHub API to display your id
"""
import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    info = (username, password)
    request = requests.get(url, auth=info)
    try:
        print(request.json()['id'])
    except Exception:
        print('None')
