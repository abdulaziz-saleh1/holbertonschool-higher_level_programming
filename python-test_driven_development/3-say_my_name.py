#!/usr/bin/python3
"""
Module prints fist name and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Function prints first and last name

    Args:
        first_name(str):
        last_name(str):

    Returns:
        Returns first and last name.
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
