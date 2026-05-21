# Create a base class Animal with a method sound(). Create a derived class Dog
# that overrides the sound() method. Demonstrate method overriding.
#
# class Animal:
#     def sound(self):
#         print("animals make sounds")
# class Dog(Animal):
#     def sound(self):
#         print("dog barks")
# obj=Dog()
# obj.sound()
\
#
#
#
# class A:
#     def show(self):
#         print("inside a")
# class B(A):
#     def show(self):
#         print("Inside b")
#         super().show()
# obj=B()
# obj.show()
# class A:
#     def display(self):
#         print("A")
# class B(A):
#     def display(self):
#         super().display()
#         print("B")
# class C(B):
#     def display(self):
#         super().display()
#         print("c")
# obj=C()
# obj.display()
# print(C.mro())
# class Vehicle:
#     def wheels(self):
#         print("any vehicle has wheels")
# class Car(Vehicle):
#     def wheels(self):
#         super().wheels()
#         print("car has 4 wheels")
# class Bike(Vehicle):
#     def wheels(self):
#         super().wheels()
#         print("bike has 2 ")
# obj=Bike()
# obj1=Car()
# obj.wheels()
# obj1.wheels()
# print(Bike.mro())
# print(Car.mro())
# class Employee:
#     def __init__(self,base_s):
#         self.base_s=base_s
#     def salary(self):
#         return self.base_s
# class Manager(Employee):
#     def __init__(self,base_s,incentive):
#         super().__init__(base_s)
#         self.incentive=incentive
#     def salary(self):
#         total=super().salary()+self.incentive
#         return total
# e=Employee(30000)
# print("salary:",e.salary())
# m=Manager(50000,10000)
# print("salary:",m.salary())
from sklearn.metrics import balanced_accuracy_score


# class MathOps:
#     def add(a,b):
#         return a+b
# class AdvancedOps(MathOps):
#     pass
# result=AdvancedOps.add(10,20)
# print(result)
#
# class Father:
#     def __init__(self, fname):
#         self.fname = fname
#
#     def skills(self):
#         print("Father Skills: Gardening, Driving")
#
#
# class Mother:
#     def __init__(self, mname):
#         self.mname = mname
#
#     def skills(self):
#         print("Mother Skills: Cooking, Painting")
#
#
# class Child(Mother, Father):
#     def __init__(self, fname, mname, cname):
#
#         super().skills()
#         self.cname = cname
# obj = Child("Ramesh", "Sita", "Rahul")
# obj.skills()
# print("MRO:", Child.__mro__)




# class Person:
#     def __init__(self,name):
#         self.name=name
# class Student(Person):
#     def __init__(self,name,no):
#         super().__init__(name)
#         self.no=no
# obj=Student("mani","21s")
# print(obj.name)
# print(obj.no)


# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#
#
# r = Rectangle(10, 5)
#
# print("Area of Rectangle:", r.area())
#encapsulation
#1
# class BankAccount:
#     def __init__(self,accountno,balance):
#         self.accountno=accountno
#         self.__balance=balance
#     def deposite(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print("successfull",self.__balance)
#         else:
#             print("the deposite amount must be positive")
#     def withdraw(self,amount):
#         if amount<0:
#             print("withdraw amount must be positive")
#
#         elif amount>self.__balance:
#             print("insufficent balance")
#         else:
#             self.__balance-=amount
#             print("withdraw sucessfull remaining amount is",self.__balance)
#     def p(self):
#         return self.__balance
# a=BankAccount("12345",3000)
# a.deposite(300)
# a.withdraw(400)
# print(a.p())

#2

# class Student:
#     def __init__(self,name,marks=0):
#         self.name=name
#         self.__marks=marks
#     def set_marks(self,marks):
#         if 0<=marks<=100:
#             self.__marks = marks
#             print("undated")
#         else:
#             print("not updated")
#     def get_marks(self):
#         return self.__marks
# s=Student("a")
# s.set_marks(89)
# print(s.get_marks())
# s.set_marks(160)


#
# #3
# class Secure:
#     def __init__(self,content,password):
#         self.__content=content
#         self.__password=password
#         self.log=[]
#     def read(self,password):
#         if password==self.__password:
#             return self.__content
#         else:
#
#             return "accues denied"
#     def __get_log(self):
#         return self.__log
# a=Secure("top secret","1234")
# print(a.read("1234"))
# print(a.read("1111"))
# print(a.read("0000"))

#4
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#         self.__access_log = []
#     def get_salary(self):
#         self.__access_log.append("Salary accessed")
#         print("Access logged.")
#         return self.__salary
#     def update_salary(self, new_salary):
#         if new_salary > self.__salary:
#             self.__salary = new_salary
#             print("Salary updated successfully.")
#         else:
#             print("New salary must be higher than current salary.")
#     def view_logs(self):
#         return self.__access_log
# emp1 = Employee("Manaswitha", 50000)
# print(emp1.get_salary())
# emp1.update_salary(60000)
# emp1.update_salary(55000)
# print(emp1.view_logs())


#
# #5
# class Product:
#     def __init__(self,name,price,discount):
#         self.name=name
#         if price<0:
#             raise ValueError("not correct price")
#         self.__price=price
#         if discount<0 or discount>70:
#             raise ValueError("no discount execeded more than 70%")
#         self.__discount=discount
#     def __calculate(self):
#         return self.__price - (self.__price * self.__discount / 100)
#     def get_final(self):
#         return self.__calculate()
# p1 = Product("Laptop", 50000, 20)
# print(p1.get_final())


#6
# class Character:
#     def __init__(self,max_health):
#         self.__max_health=max_health
#         self.__health=max_health
#     @property
#     def health(self):
#         return self.__health
#     def damange(self,points):
#         if points<0:
#             print("health points cant be negitive")
#             return
#         self.__health-=points
#         if self.__health<0:
#             self.__health=0
#     def heal(self,points):
#         if points<0:
#             print("health points cant be negitive")
#             return
#         self.__health+=points
#         if self.__health>self.__max_health:
#             self.__health=self.__max_health
# c=Character(100)
# print(c.health)
# c.damange(40)
# print(c.health)
# c.heal(100)
# print(c.health)

#7
# class Engine:
#     def __init__(self):
#         self.__temp=25
#     def start(self):
#         self.__temp+=50
#         print("engine started")
#     def cool(self):
#         if self.__temp>25:
#             self.__temp-=30
#             print("engine is colling")
#         else:
#             print("enginee is alredy in cool state")
#     def get_temp(self):
#         return self.__temp
# class Car:
#     def __init__(self):
#         self.__engine=Engine()
#     def start_car(self):
#         print("starting car")
#         self.__engine.start()
#     def cool_engine(self):
#         self.__engine.cool()
#     def show_temp(self):
#         print("temp=",self.__engine.get_temp())
# a=Car()
# a.start_car()
# # a.show_temp()
# a.cool_engine()
# a.show_temp()

#8

# class ShoppingCart:
#     def __init__(self):
#         self.__items=[]
#     def add_item(self,item):
#         self.__items.append(item)
#     def remove_item(self,item):
#         if item in self.__items:
#             self.__items.remove(item)
#             print(f"{item} is removed")
#         else:
#             print(f"{item} not found")
#     def get_items(self):
#         return self.__items.copy()
# c=ShoppingCart()
# c.add_item("laptop")
# c.add_item("house")
# print(c.get_items())
# items=c.get_items()
# c.add_item("me")
# print(c.get_items())

#9
