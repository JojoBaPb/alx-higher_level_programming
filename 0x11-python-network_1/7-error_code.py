#!/usr/bin/python3
"""Script that:
- takes in URL
- sends request to URL
- displays body of response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
