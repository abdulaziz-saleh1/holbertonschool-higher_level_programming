#!/usr/bin/env python3
"""
Defines mixins SwimMixin, FlyMixin, and a Dragon class using them.
"""

class SwimMixin:
    """
    Mixin that adds swimming ability.
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin that adds flying ability.
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that can swim and fly using mixins.
    """
    def roar(self):
        print("The dragon roars!")


# Testing
if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
