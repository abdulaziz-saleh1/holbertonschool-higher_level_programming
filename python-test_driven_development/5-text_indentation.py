#!/usr/bin/python3
"""
This function takes text as an argument, loop through it and if
it it read any of these characters ., ? and :, it will go to the next line
"""


def text_indentation(text):
    """
    a function that goes to newline after ., ? and :

        Args:
        Text: the text to be parised

    Returns:
        None

    Raises:
        "TypeError": if text is not a string type

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    index = 0
    while index < len(text):
        print(text[index], end="")
        if text[index] in ".?:":
            print("\n\n", end="")
            while index + 1 < len(text) and text[index+1] == " ":
                text = text[:index+1] + text[index+2:]
        index += 1
