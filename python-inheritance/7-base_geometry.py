#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """BaseGeometry class with area method."""

    def area(self):
        """Raise exception if area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
