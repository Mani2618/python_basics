#1
# Create a class Person whose constructor takes age as an argument. Raise a
# ValueError if the age is less than 0.
# class Person:
#     def __init__(self,age):
#         if age<0:
#             raise ValueError("age can't be negitive")
#         self.age=age
# try:
#     p1=Person(25)
#     print("age:",p1.age)
#     p2 = Person(-5)
# except ValueError as e:
#     print("Error:", e)

# 3
# Create a class Student with an attribute marks. Implement a method
# set_marks(marks) that raises a ValueError if marks are not in the range 0 to
# 100
# class Student:
#     def __init__(self):
#         self.marks=0
#     def set_marks(self,marks):
#         if marks<0 or marks>100:
#             raise ValueError("marks can't be negitive or more than 100")
#         self.marks=marks
# s1=Student()
# try:
#     s1.set_marks(-5)
# except ValueError as e:
#     print("error:",e)

#4


# Create a custom exception named InvalidAgeError.Create a class Voter with a method check_eligibility(age)
# that raises  this exception if age is less than 18.
# class InvalidAgeError(Exception):
#     pass
# class Voter:
#     def check_eligibility(self,age):
#         if age<18:
#             raise InvalidAgeError("age cant be les than 18")
#         print("Eligible to vote")
# v=Voter()
# try:
#     v.check_eligibility(16)
# except InvalidAgeError as e:
#     print("error",e)

#5
# • Create a class BankAccount with an attribute balance. Implement a method
# withdraw(amount) that raises an exception if the withdrawal amount is greater
# than the available balance.
#
# class BankAccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         if amount>self.balance:
#             raise ValueError("withdraw amount can't be more than the balance")
#         else:
#             self.balance-=amount
#             print("self.balance")
# a=BankAccount(1000)
# try:
#     a.withdraw(1100)
# except ValueError as e:
#     print("error",e)

# Create a class PasswordValidator with a method validate(password). Raise an
# exception if the password length is less than 8 characters.
# class PasswordValidator:
#     def validate(self,password):
#         if len(str(password))<8:
#             raise Exception("password should have 8 chars")
#         else:
#             print("password is valid")
# a=PasswordValidator()
# try:
#     a.validate(1234)
# except Exception as e:
#     print("Error:",e)
# Create a class UserInput with a method get_integer(value). Handle ValueError
# and TypeError using separate except blocks
# class UserInput:
#     def get_integer(self,value):
#         try:
#             n=int(value)
#             print("Integer value",n)
#         except ValueError:
#             print("Invalid value error")
#         except TypeError:
#             print("Invalid Type error")
# a=UserInput()
# a.get_integer(10)
# a.get_integer("10-a")
# a.get_integer(None)
# Create a base class Shape with a method area() that raises
# NotImplementedError. Create a child class Rectangle that overrides and
# implements the area method.
# class Shape:
#     def area(self):
#         raise NotImplementedError("not yet")
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         return self.l*self.b
# a=Rectangle(5,6)
# print("area is:",a.area())
# s = Shape()
# print(s.area(1))
# Create a class Service with a method that calls another method which raises an
# exception. Catch and handle the exception in the Service class
# class Service:
#     def a(self):
#         raise ValueError("not known")
#     def b(self):
#         try:
#             self.a()
#         except ValueError as e:
#             print("error:",e)
# s=Service()
# s.b()
# Create a class Transaction with a method process() that uses try, except, and
# finally blocks to ensure a cleanup message is always printed.
# class Transaction:
#     def process(self,amount):
#         try:
#             print("transaction is in process")
#             if amount<=0:
#                 print("invalid amount")
#             else:
#                 print("transaction sucessfull")
#         except ValueError as e:
#             print("Error:",e)
#         finally:
#             print("cleanup message: all the data is cleaned properly")
# a=Transaction()
# a.process(100)
# a.process(-10)
# Create a class LoginSystem with a method login(password) that raises an
# exception for an incorrect password and handles the exception outside the class.
# class LoginSystem:
#     def __init__(self,password):
#         self.password=password
#     def login(self,new):
#         if new!=self.password:
#             raise ValueError("Incorrect password")
#         else:
#             print("login successful")
# a=LoginSystem("@Ammu2005")
# try:
#     a.login("12345667")
# except ValueError as e:
#     print("error:",e)


