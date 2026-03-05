class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayinfo(self):
        return "Name: " + self.name + ", Age: " + str(self.age)


class Student(Person):
    def displayinfo(self):
        return Person.displayinfo(self) + ", Grade: " + self.grade


student = Student("John", 15)  # uses Person __init__
student.grade = "10th"         # set grade after

print(student.displayinfo())

# add 2 attributes that are not in human class # 