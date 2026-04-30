class Daniel_k20250941_Olivier_K20250907(Exception):
    pass

class CMP142:
    def __init__(self, attendance):
        self.attendance = attendance

    def check_quiz(self, num_students):
        if num_students < 16:
            print("No quiz, too few students in class.")

        if num_students >= 16:
            print("Get ready for quiz !")
    
c1 = CMP142(attendance=16)

try:
    attendance = float(input("Enter number of students: "))
    c1.check_quiz(attendance)

finally:
    print("Thank you for attendance")

# File for Daniel and Olivier!!