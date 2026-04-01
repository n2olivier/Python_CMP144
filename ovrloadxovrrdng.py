class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Bark")  # overrides parent method


# ---------- Method Overloading ----------

class Math:
    def add(self, a, b, c=0):  # default argument used
        print("Sum:", a + b + c)


# ---------- Usage ----------

# overriding
animal = Animal()
dog = Dog()

animal.sound()
dog.sound()

# overloading
math = Math()
math.add(2, 3)        # 2 arguments
math.add(2, 3, 4)     # 3 arguments