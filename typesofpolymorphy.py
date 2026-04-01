# file: polymorphism_multilevel_hybrid.py

# ---------- Multilevel Inheritance ----------

class Animal:
    def sound(self):
        print("Some sound")


class Mammal(Animal):
    pass


class Dog(Mammal):
    def sound(self):
        print("Bark (Multilevel)")


# ---------- Hybrid Inheritance ----------

class Walker:
    def move(self):
        print("Walking")


class Cat(Animal, Walker):
    def sound(self):
        print("Meow (Hybrid)")


# ---------- Usage ----------

# multilevel polymorphism
dog = Dog()
dog.sound()

# hybrid polymorphism
cat = Cat()
cat.sound()
cat.move()