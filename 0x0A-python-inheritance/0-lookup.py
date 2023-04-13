#!/usr/bin/python3
"""Defines attribute lookup function."""


def lookup(obj):
    """Returns list of object's available attributes."""
    return (dir(obj))

