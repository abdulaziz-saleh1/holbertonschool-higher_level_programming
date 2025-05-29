#!/usr/bin/python3
"""
    Function that prints "My name is <first name> <last name>"
"""

def say_my_name(first_name, last_name=""):
    """
    Prints a formatted name message.

    Args:
        first_name: The first name (str).
        last_name: The last name (str, optional).

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
