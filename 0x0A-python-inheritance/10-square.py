#!/usr/bin/python3
"""Defines a Rect subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): Size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
