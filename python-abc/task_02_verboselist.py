#!/usr/bin/env python3
"""
Defines the VerboseList class, extending the built-in list with notifications.
"""

class VerboseList(list):
    """
    Custom list that prints notifications for append, extend, remove, and pop operations.
    """

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
