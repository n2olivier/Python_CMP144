from abc import ABC, abstractmethod


class vehicles(ABC):
    def __init__(self, tires):
        self.tires = tires

    @abstractmethod
    def start(self):
        pass

    def display(self):
        print("Vehicle with", self.tires, "tires")


class Bike(vehicles):
    def __init__(self, colour):
        super().__init__(2)
        self.colour = colour

    def start(self):
        print("Start with the kick")

    def show_colour(self):
        print("Bike colour is", self.colour)


class Car(vehicles):
    def __init__(self, brand, colour):
        super().__init__(4)
        self.brand = brand
        self.colour = colour

    def start(self):
        print("Start with the key")

    def show_brand(self):
        print("Car brand is", self.brand)

    def show_colour(self):
        print("Car colour is", self.colour)

bike1 = Bike("mango")
car1 = Car("Toyota", "Black")

bike1.display()
bike1.start()
bike1.show_colour()

print()

car1.display()
car1.start()
car1.show_brand()
car1.show_colour()