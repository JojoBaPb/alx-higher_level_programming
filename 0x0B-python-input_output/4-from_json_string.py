#!/usr/bin/python3
"""Defines JSON to object function."""
import json


def from_json_string(my_str):
    """Returns Python object of JSON string."""
    return json.loads(my_str)
