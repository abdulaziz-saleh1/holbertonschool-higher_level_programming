#!/usr/bin/python3
"""Module for MyList class."""

class MyList(list):
    """A subclass of list with a method to print it sorted."""

    def print_sorted(self):
        """Prints the list sorted."""
        print(sorted(self))
