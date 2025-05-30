#!/usr/bin/python3
"""An improved BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Method not implemented."""
        raise Exception("area() is not implemented")
