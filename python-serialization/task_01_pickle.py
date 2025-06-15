#!/usr/bin/python3
"""Module for serializing and deserializing a custom Python object
using the pickle module.
"""


import pickle


class CustomObject:
    """A class representing a custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes in a specific format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the object and saves it to the specified file."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass  # Optionally, log error or notify

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from the specified file."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
