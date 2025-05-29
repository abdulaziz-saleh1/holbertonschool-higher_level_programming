#!/usr/bin/python3
"""
Module prints new lines after chars..
"""


def text_indentation(text):
    """
    Function prints 2 new lines after chars ., ? and :

    Args:
        text(str):

    Returns:

    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    chars = '.?:'

    if '.' not in text and '?' not in text and ':' not in text:  # check..
        print(text, end="")
    iter_index = 0
    max_index = len(text) - 1
    for index, value in enumerate(text):
        if value in chars:
            print(text[iter_index:index + 1])
            print()
            iter_index = index
            if index < max_index and text[index + 1] == " ":
                iter_index = index + 2
                if '.' not in text[iter_index:] and ':' not in \
                        text[iter_index:] and '?' not in text[iter_index:]:
                    print(text[iter_index:len(text)], end="")
                    break
            if iter_index < max_index and text[index + 1] is not " ":
                iter_index = index + 1
                if '.' not in text[iter_index:] and ':' not in \
                        text[iter_index:] and '?' not in text[iter_index:]:
                    print(text[iter_index:len(text)], end="")
                    break
