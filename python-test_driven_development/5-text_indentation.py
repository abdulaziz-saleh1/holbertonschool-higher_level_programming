#!/usr/bin/python3
"""
This function takes text as an argument, loop through it and if
it reads any of these characters ., ? and :, it will go to the next line
"""


def text_indentation(text):
    """
    a function that goes to newline after ., ? and :

    Args:
        text: the text to be parsed

    Returns:
        None

    Raises:
        TypeError: if text is not a string type
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0
    while index < len(text):
        print(text[index], end="")
        if text[index] in ".?:":
            print()
            print()
            while index + 1 < len(text) and text[index + 1] == " ":
                index += 1
        index += 1
