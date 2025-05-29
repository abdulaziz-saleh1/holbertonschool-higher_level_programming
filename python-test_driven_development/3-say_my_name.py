#!/usr/bin/python3
"""
A function that prints: My name is <first name> <last name>
"""

def say_my_name(first_name, last_name=""):
    """
    Prints: My name is <first name> <last name>

    Args:
        first_name: first name, must be a string
        last_name: last name, must be a string

    Raises:
        TypeError: if first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
