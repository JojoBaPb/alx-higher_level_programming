#!/usr/bin/python3
"""Defines JSON file writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes object to text file using JSON form."""
    with open(filename, "x") as f:
        json.dump(my_obj, f)
