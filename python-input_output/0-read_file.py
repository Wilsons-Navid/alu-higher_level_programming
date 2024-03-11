#!/usr/bin/python3
"""Defines a function to read and print the contents of a UTF-8 text file."""


def read_file(filename=""):
    """Print the contents of a UTF-8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
