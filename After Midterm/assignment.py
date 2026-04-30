# Custom Exception Class
class Daniel_k20250941_Olivier_K20250907(Exception):
    pass


# Quiz Class
class Quiz:
    def __init__(self, attendance):
        self.attendance = attendance

    def start_quiz(self):
        if self.attendance < 10:
            raise Daniel_k20250941_Olivier_K20250907("Too few students for Quiz")
        print("Quiz Time!")


# Midterm Class
class Midterm:
    def __init__(self, attendance):
        self.attendance = attendance

    def start_midterm(self):
        if self.attendance < 20:
            raise Daniel_k20250941_Olivier_K20250907("Too few students for Midterm")
        print("Midterm Time!")


# Final Class
class Final:
    def __init__(self, attendance):
        self.attendance = attendance

    def start_final(self):
        if self.attendance < 30:
            raise Daniel_k20250941_Olivier_K20250907("Too few students for Final Exam")
        print("Final Exam Time!")


try:
    attendance = float(input("Enter number of students: "))

    if attendance >= 30:
        f1 = Final(attendance)
        f1.start_final()

    elif attendance >= 20:
        m1 = Midterm(attendance)
        m1.start_midterm()

    elif attendance >= 10:
        q1 = Quiz(attendance)
        q1.start_quiz()

    else:
        raise Daniel_k20250941_Olivier_K20250907(
            "No Quiz, No Midterm, No Final"
        )

except Daniel_k20250941_Olivier_K20250907 as e:
    print("Error:", e)

finally:
    print("Thank you for attendance")