#!/usr/bin/python3
"""Define a txt file read function."""


def read_file(filename=""):
    """Prints content of UTF8 txt to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
