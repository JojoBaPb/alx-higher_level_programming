#!/usr/bin/python3
"""
contains MyList class
"""


class MyList(list):
    """enables printing for the built in list class."""

    def print_sorted(self):
        """Prints a list in ascending order."""
        print(sorted(self))
