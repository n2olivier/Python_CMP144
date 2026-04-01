# file: encapsulation_example.py

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # private variable (name mangling)

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

    def get_marks(self):
        return self.__marks


# create object
student1 = Student("Ali", 85)

# try direct access (not recommended)
try:
    print(student1.__marks)
except AttributeError:
    print("Cannot access private variable directly!")

# access using method
print("Marks (getter):", student1.get_marks())

# update marks using setter
student1.set_marks(90)
print("Updated Marks:", student1.get_marks())

# name mangling access (advanced)
print("Access using name mangling:", student1._Student__marks)