#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
