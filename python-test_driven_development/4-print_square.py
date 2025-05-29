#!/usr/bin/python3
"""
Module prints a square with the character "#"
"""


def print_square(size):
    """
    Prints a square of symbol, '#' to the stdout..

    Args:
        size(int):

    Returns:
        A square of '#'
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for m in range(size):
        for m in range(size):
            print('#', end="")
        print()
