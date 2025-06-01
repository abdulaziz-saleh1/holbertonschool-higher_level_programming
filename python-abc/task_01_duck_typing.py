#!/usr/bin/env python3
"""
Abstract Shape class with Circle and Rectangle subclasses.
"""

from abc import ABC, abstractmethod
import math

"""
Abstract base class Shape with abstract methods area and perimeter.
"""
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


"""
Circle subclass that implements area and perimeter.
"""
class Circle(Shape):
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


"""
Rectangle subclass that implements area and perimeter.
"""
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.height + self.width)


"""
Function that prints the area and perimeter of a shape.
"""
def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
