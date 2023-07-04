#!/usr/bin/python3
"""Script fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
