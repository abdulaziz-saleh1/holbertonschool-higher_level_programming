#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the sum as an integer.

    Args:
        a: first integer or float
        b: second integer or float (default 98)

    Returns:
        int: The addition of a and b as integer.

    Raises:
        TypeError: if a or b are not integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
