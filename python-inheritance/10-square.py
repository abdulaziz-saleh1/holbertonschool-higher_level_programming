#!/usr/bin/python3
"""
Module that defines a Square class inheriting from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that initializes size, validated as width and height.
    """

    def __init__(self, size):
        """
        Initialize Square with size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
