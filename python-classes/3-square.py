#!/usr/bin/python3

"""create a class Square with a private instance size"""


class Square:

    """create a class an instance attribute of the class"""

    def __init__(self, size=0):
        """"handle Errors"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
