#!/usr/bin/python3
"""Defines base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsents base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates param as an int.

        Args:
            name (str): name of param.
            value (int): param to validate.
        Raises:
            TypeError: value is not an int.
            ValueError: value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
