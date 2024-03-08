#!/usr/bin/python3


"""Creating a rectangle classs"""


class Rectangle:

    """initializing width and height"""

    def i__init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value
    
    @property
    def height(self):
        return self._Rectangle__height
    
    @height.setter
    def height(self, value):
        if type(value) is not  int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
