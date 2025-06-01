#!/usr/bin/python3
from abc import ABCMeta, abstractmethod
import math

"""
Abstract Shape class with area and perimeter methods.
"""

class Shape(metaclass=ABCMeta):
    """
    Base abstract shape class.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


"""
Circle class that implements area and perimeter.
"""

class Circle(Shape):
    """
    Circle with radius.
    """
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


"""
Rectangle class that implements area and perimeter.
"""

class Rectangle(Shape):
    """
    Rectangle with width and height.
    """
    def __init__(self, width, height):
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)


"""
Function to print area and perimeter of a shape.
"""

def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
