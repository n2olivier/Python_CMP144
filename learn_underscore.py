class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayinfo(self):
        return "Name: " + self.name + ", Age: " + str(self.age)


class Student(Person):
    def __init__(self, name, age, grade, school):
        Person.__init__(self, name, age)   # calling parent constructor
        self.grade = grade
        self.school = school

    def displayinfo(self):
        return Person.displayinfo(self) + ", Grade: " + self.grade + ", School: " + self.school


student = Student("John", 15, "10th", "Central High")

print(student.displayinfo())