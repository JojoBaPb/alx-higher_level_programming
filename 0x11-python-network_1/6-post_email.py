#!/usr/bin/python3
"""Script:
- takes in URL and email address
- sends POST req to passed URL with email as param
- displays body of response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    req = requests.post(url, data=value)
    print(r.text)
