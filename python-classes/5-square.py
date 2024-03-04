#!/usr/bin/python3



class Square:
    def __init__(self, size=0):
        self._size = size
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self._size = value
        
    def area(self):
        return self._size * self._size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
