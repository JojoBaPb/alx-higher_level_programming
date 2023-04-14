#!/usr/bin/python3
"""Defines class MyInt that is inherited from int."""


class MyInt(int):
    """Inverse int ops == and !=."""

    def __eq__(self, value):
        """Override == op with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != op with == behavior."""
        return self.real == value
