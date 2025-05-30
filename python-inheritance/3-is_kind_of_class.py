#!/usr/bin/python3
"""
A module with is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or inherits from it.
    """
    return isinstance(obj, a_class)
