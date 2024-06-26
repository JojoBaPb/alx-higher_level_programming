#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
    """Init new Rect.
    width (int): Width new rectangle
    height (int): Height new rectangle.
    """
    self.width = width
    self.height = height

    @property
    def width(self):
        """set width Rect."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of Rect."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perim of Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return printable rep of Rect.

        The rect with # char.
        """
        if self.__width == 0 or self.__height = 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append("#") for y in range(self.__width)]
            if x != self.__height -1:
                rect.append("\n")
        return ("".join(rect))
