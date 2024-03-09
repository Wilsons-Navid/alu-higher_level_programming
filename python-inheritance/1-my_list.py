#!/usr/bin/python3


"""Inherits properties form a classs"""

class MyList(list):

    """Creates a method init"""
    def __init__(self):

        """Init of parent class"""
        super.__init__()

    def print_sorted(self):

        """Sorted list"""

        print(sorted(self))
