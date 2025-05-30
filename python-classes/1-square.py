#!/usr/bin/python3
"""Defines a square class with a private instance attribute."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
