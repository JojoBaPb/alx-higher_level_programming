#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
        """defines class Rectangle with width and height var"""

def __init__(self, width=0, height=0):
    """initiates class instance with width height"""
    self.width = width
    self.height = height

    @property
    def width(self):
        """gets width instance"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets width instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets height instance"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets height instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
