#!/usr/bin/env python3
"""
Defines the CountedIterator class that keeps track of the number of items iterated.
"""

class CountedIterator:
    """
    Iterator that counts how many items have been iterated over.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.
        """
        self.iterator = iter(iterable)  # Create an iterator from the iterable
        self.count = 0                  # Initialize counter

    def get_count(self):
        """
        Return the number of items that have been iterated over.
        """
        return self.count

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.
        Raise StopIteration when no more items.
        """
        item = next(self.iterator)  # This may raise StopIteration if done
        self.count += 1             # Increment the counter
        return item

    def __iter__(self):
        """
        Return self to make this object itself an iterator.
        """
        return self
