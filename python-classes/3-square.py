#!/usr/bin/python3

class Square:

    """create a class Square with a private instance size"""

    def __init__(self, size=0):
        """"handle Errors"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self._size = size

    def area(self):
       return size*size
