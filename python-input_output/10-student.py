#!/usr/bin/python3

class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, includes only those attributes in the dictionary.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
