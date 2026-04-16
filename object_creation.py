# Simple illustration of creating an object in Python

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an object (instance)
my_dog = Dog("Buddy")

# Using the object
my_dog.bark()

