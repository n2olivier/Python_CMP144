class Fruit:
    def __init__(self, taste, season, color):
        self.color = color        # public
        self._taste = taste       # protected (convention)
        self.__password = season  # private (name mangling)

    def call(self):
        return "The " + self.color + " fruit is available in " + self.__password

# Create object
f = Fruit("Sweet", "Summer", "Red")

print(f.color)          
print(f._taste)          
print(f._Fruit__password)
print(f._Fruit__password)
# self is the instance of the class
