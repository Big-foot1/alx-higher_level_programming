#!/usr/bin/python3
"""
takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    try:
        ar = sys.argv[1]
    except Exception:
        ar = ""
    q = {"q": ar}
    r = requests.post(url, data=q)
    try:
        result = r.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print("[{}] {}".format(result['id'], result['name']))
    except Exception:
        print("No result")
