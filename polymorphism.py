# file: polymorphism_simple.py

class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


# create objects
dog = Dog()
cat = Cat()

# polymorphism in action
animals = [dog, cat]

for animal in animals:
    animal.sound()