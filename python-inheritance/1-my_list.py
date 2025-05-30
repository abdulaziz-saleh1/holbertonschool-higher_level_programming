#!/usr/bin/python3
"""
This module defines MyList class that inherits from list
and adds a print_sorted() method.
"""


class MyList(list):
    """
    MyList is a subclass of list with a method to print the
    list's elements in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort).
        """
        print(sorted(self))
