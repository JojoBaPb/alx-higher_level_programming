#!/usr/bin/python3
"""Define file-writing func."""


def write_file(filename="", text=""):
    """Writes string to a UTF8 text file.

    Args:
        filename (str): name of file to write.
        text (str): text to write to file.
    Returns:
        number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
