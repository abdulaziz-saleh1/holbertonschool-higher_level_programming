#!/usr/bin/python3
"""
This module defines a function that adds two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    if isinstance(a, float):
        if a != a:  # NaN check
            raise ValueError("cannot convert float NaN to integer")
        if a in (float('inf'), -float('inf')):
            raise OverflowError("cannot convert float infinity to integer")
    
    if isinstance(b, float):
        if b != b:
            raise ValueError("cannot convert float NaN to integer")
        if b in (float('inf'), -float('inf')):
            raise OverflowError("cannot convert float infinity to integer")

    if a is None:
        raise ValueError("a must be an integer")
    if b is None:
        raise ValueError("b must be an integer")

    return int(a) + int(b)
