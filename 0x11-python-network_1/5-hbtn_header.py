#!/usr/bin/python3
"""Displays value of var X-Request-Id header
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(r.headers.get("X-Request-Id"))
