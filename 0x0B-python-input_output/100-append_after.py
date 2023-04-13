#!/usr/bin/python3
"""Defines text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line with given string in file.

    Args:
        filename (str): Name of the file.
        search_string (str): String that searches within the file.
        new_string (str): String to be inserted.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
