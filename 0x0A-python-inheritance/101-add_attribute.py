#!/usr/bin/python3
"""Defines func that adds attri to objs."""


def add_attribute(obj, att, value):
    """Adds new attribute to obj if possible.

    Args:
        obj (any): Object to add attribute to.
        att (str): Name of attribute to add to obj.
        value (any): Value of att.
    Raises:
        TypeError: If attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
