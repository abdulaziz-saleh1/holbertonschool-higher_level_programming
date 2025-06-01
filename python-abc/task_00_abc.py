#!/usr/bin/python3
from abc import ABCMeta, abstractmethod
"""
Defines an abstract Animal class and its concrete subclasses Dog and Cat.
"""



class Animal(metaclass=ABCMeta):
    """
    The abstract base class Animal defines an abstract method sound().
    Subclasses must implement this method.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Concrete subclass Dog that implements the sound() method.
    """
    def sound(self):
        """
        Returns the sound made by the dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete subclass Cat that implements the sound() method.
    """
    def sound(self):
        """
        Returns the sound made by the cat.
        """
        return "Meow"
