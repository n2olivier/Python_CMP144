# Simple Inheritance Illustration for Beginners - Friendly Animals!

class Animal:  # Parent class (base)
    def __init__(self, name):
        self.name = name  # All animals have a name
    
    def eat(self):
        print(f"{self.name} is eating.")

class Rabbit(Animal):  # Child class inherits from Animal
    def hop(self):  # Rabbit can hop (extra ability)
        print(f"{self.name} hops happily!")

class Turtle(Animal):  # Another child class inherits from Animal  
    def swim(self):  # Turtle can swim (extra ability)
        print(f"{self.name} swims slowly.")

# Create child objects - they automatically get parent's abilities!
bunny = Rabbit("Bunny")
shelly = Turtle("Shelly")

# Parent abilities work!
bunny.eat()   # From Animal
shelly.eat()  # From Animal

# Child unique abilities
bunny.hop()   # Only Rabbit
shelly.swim() # Only Turtle

# Output:
# Bunny is eating.
# Shelly is eating.
# Bunny hops happily!
# Shelly swims slowly.

