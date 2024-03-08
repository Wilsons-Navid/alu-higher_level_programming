#!/usr/bin/python3


"""creating a class that calculates the are and perimeter of the rectangle"""


class Rectangle:

    """Creates the function that initialises the width and length"""

    def __init__(self, height=0, width=0):
        self.width = width
        self.height = height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return 2 * (self.height + self.width)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an interger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an interger")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
