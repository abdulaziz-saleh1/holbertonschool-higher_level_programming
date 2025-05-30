#!/usr/bin/python3
"""
A module that defines a function to check
if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.

    Args:
        obj: object to check.
        a_class: class to compare.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
