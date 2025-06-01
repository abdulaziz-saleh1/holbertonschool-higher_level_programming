#!/usr/bin/env python3
"""
Defines classes Fish, Bird, and FlyingFish to explore multiple inheritance.
"""

class Fish:
    """
    Class representing a Fish.
    """
    def swim(self):
        print("The fish is swimming!")

    def habitat(self):
        print("The fish lives in water!")


class Bird:
    """
    Class representing a Bird.
    """
    def fly(self):
        print("The bird is flying!")

    def habitat(self):
        print("The bird lives in the sky!")


class FlyingFish(Fish, Bird):
    """
    Class representing a FlyingFish, inheriting from both Fish and Bird.
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# Testing
if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    # MRO
    print(FlyingFish.mro())
