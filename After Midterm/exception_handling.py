# def withdrawal(balance: float, amount: float) -> float:
#     if amount <= 0:
#         raise ValueError("Amount must be greater than 0")
#     if amount > balance:
#         raise ValueError("Insufficient balance")
#     return balance - amount


# try:
#     balance = 1000
#     print("Your current balance is:", balance)

#     amount = float(input("Enter withdrawal amount: "))

#     balance = withdrawal(balance, amount)
#     print("Withdrawal successful. New balance:", balance)

# except ValueError as e:
#     print("Error:", e)

# finally:
#     print("Transaction attempt complete.")

# class InsufficientBallance(Exception):
#     pass

# ------------------------------------------------------------------------

# class Wallet:
#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Amount must be greater than 0")

#         if amount > self.balance:
#             raise InsufficientBallance("Please fund your account")
#         self.balance -= amount
#         print("Transaction completed")


# m1 = Wallet(1000)

# try:
#     amount = float(input("Please input your withdrawal amount"))
#     m1.withdraw(amount)
# except InsufficientBallance as e:
#     print("Mustafa please go and top-up:", e)
# -----------------------------------------------------------------------------------------------------
class Students(Exception):
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