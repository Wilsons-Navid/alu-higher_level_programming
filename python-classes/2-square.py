#!/usr/bin/python3

"""Creating class"""

class Square:

    """Initializing a class attribute"""
    def __init__(self, size = 0):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self._size = size
