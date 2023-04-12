#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
                    
        Args:
        first_name (str): first name of student.
        last_name (str): last name of student.
        age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only attris
        included in list.
                                                                                                                        
        Args:
        attrs (list): (Optional) attributes to represent.
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attr of the Student.

        Args:
        json (dict): The key/value to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
