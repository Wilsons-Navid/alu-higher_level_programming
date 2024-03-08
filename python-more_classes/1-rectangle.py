#!/usr/bin/python3


"""Creating a rectangle classs"""


class Rectangle:

    """initializing width and height"""

    def __init__(self, width  = 0, height = 0):
        self.width = width
        self.length = length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._height = value
