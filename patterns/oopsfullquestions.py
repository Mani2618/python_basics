# Design a banking system with:
# • An abstract base class Account with deposit(), withdraw(),
# calculate_interest().
# • Subclasses: SavingsAccount, CurrentAccount, FixedDepositAccount.
# • Each account must:
# o Encapsulate balance (private)
# o Provide controlled access through properties
# o Override interest calculation differently
# • Include a static method to validate amount.
# • Include a class method to update bank-wide interest policies
# from abc import ABC,abstractmethod
# class Account(ABC):
#     interest=0.05
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=0
#     @property
#     def balance(self):
#         return self.__balance
#
#     @staticmethod
#     def validate_amount(amount):
#         return amount>0
#     @classmethod
#     def update(cls,new):
#         cls.interest=new
#     def deposite(self,amount):
#         if self.validate_amount(amount):
#             self.__balance+=amount
#         else:
#             print("Invalid")
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#         else:
#             print("amount should be less than balance amount to wothdraw")
#     @abstractmethod
#     def calculate_interest(self):
#         pass
# class SavingsAccount(Account):
#     def calculate_interest(self):
#         return self.balance*Account.interest
# class CurrentAccount(Account):
#     def calculate_interest(self):
#         return self.balance*0.06
# class FixedDepositAccount(Account):
#     def calculate_interest(self):
#         return self.balance*0.75
# a1 = SavingsAccount("Manu", 10000)
# a2 = CurrentAccount("Ravi", 15000)
# a3 = FixedDepositAccount("Sita", 20000)
#
# accounts = [a1, a2, a3]
#
# for i in accounts:
#     print(f"{i.name} Interest: {i.calculate_interest()}")
# print("\nBalance (via property):", a1.balance)
#
# Account.update(0.1)
#
# print("\nAfter updating interest rate:")
# print("Savings Interest:", a1.calculate_interest())
# Manu Interest: 0.0
# Ravi Interest: 0.0
# Sita Interest: 0.0
#
# Balance (via property): 0
#
# After updating interest rate:
# Savings Interest: 0.0
# 2. Build:
# • Vehicle base class
# • Car, Bike, Auto subclasses
# • A Driver class that contains a Vehicle
# • A Ride class that:
# o Calculates fare differently depending on the type of vehicle (polymorphism)
# o Stores driver + vehicle combination
# o Protects internal fare formula through encapsulation
# Also:
# • Use __str__ to print readable ride summaries.
# Show how composition + polymorphism interact.
# class Vechile:
#     def fare(self,distance):
#         pass
# class Car(Vechile):
#     def fare(self,distance):
#         return distance*12
# class Bike(Vechile):
#     def fare(self,distance):
#         return distance*6
# class Auto(Vechile):
#     def fare(self,distance):
#         return distance*10
# class Driver:
#     def __init__(self,name,vehicle):
#         self.name=name
#         self.vehicle=vehicle
# class Ride:
#     def __init__(self,driver,distance):
#         self.driver=driver
#         self.distance=distance
#         self.__fare=self.calculate_fare()
#     def calculate_fare(self):
#         return self.driver.vehicle.fare(self.distance)
#
#     def __str__(self):
#         return (f"Driver: {self.driver.name}, "
#                 f"Vehicle: {self.driver.vehicle.__class__.__name__}, "
#                 f"Distance: {self.distance} km, "
#                 f"Fare: {self.__fare}")
# v1 = Car()
# v2 = Bike()
# v3 = Auto()
# d1 = Driver("Manu", v1)
# d2 = Driver("Ravi", v2)
# d3 = Driver("Sita", v3)
# r1 = Ride(d1, 10)
# r2 = Ride(d2, 10)
# r3 = Ride(d3, 10)
# print(r1)
# print(r2)
# print(r3)
#
# Driver: Manu, Vehicle: Car, Distance: 10 km, Fare: 120
# Driver: Ravi, Vehicle: Bike, Distance: 10 km, Fare: 60
# Driver: Sita, Vehicle: Auto, Distance: 10 km, Fare: 100

# 3. Create:
# • Abstract class PaymentMethod with pay(), validate()
# • Subclasses: CardPayment, WalletPayment, UPIPayment
# • Encapsulate user balance
# • Use @property to control reading available funds
# • Overload + operator to combine two payment methods into “split payment”
# • Demonstrate polymorphism through a checkout loop.
# from abc import ABC,abstractmethod
# class PaymentMethod(ABC):
#     def __init__(self,balance):
#         self.__balance=balance
#     @property
#     def balance(self):
#         return self.__balance
#     def _deduct(self,amount):
#         self.__balance-=amount
#     @abstractmethod
#     def pay(self,amount):
#         pass
#     @abstractmethod
#     def validate(self,amount):
#         pass
#     def __add__(self,other):
#         return SplitPayment(self,other)
# class CardPayment(PaymentMethod):
#     def validate(self, amount):
#         return amount <= self.balance
#     def pay(self, amount):
#         if self.validate(amount):
#             self._deduct(amount)
#             print(f"Paid {amount} using Card")
#         else:
#             print("Card: Insufficient balance")
# class WalletPayment(PaymentMethod):
#     def validate(self, amount):
#         return amount <= self.balance
#     def pay(self, amount):
#         if self.validate(amount):
#             self._deduct(amount)
#             print(f"Paid {amount} using Wallet")
#         else:
#             print("Wallet: Insufficient balance")
# class UPIPayment(PaymentMethod):
#     def validate(self, amount):
#         return amount <= self.balance
#     def pay(self, amount):
#         if self.validate(amount):
#             self._deduct(amount)
#             print(f"Paid {amount} using UPI")
#         else:
#             print("UPI: Insufficient balance")
# class SplitPayment:
#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2
#     def pay(self, amount):
#         half = amount / 2
#         print("Split Payment:")
#         self.p1.pay(half)
#         self.p2.pay(half)
# p1 = CardPayment(1000)
# p2 = WalletPayment(500)
# p3 = UPIPayment(800)
# payments = [p1, p2, p3]
# for p in payments:
#     p.pay(200)
# split = p1 + p2
# split.pay(400)
# print("Card Balance:", p1.balance)
# Paid 200 using Card
# Paid 200 using Wallet
# Paid 200 using UPI
# Split Payment:
# Paid 200.0 using Card
# Paid 200.0 using Wallet
# Card Balance: 600.0

# 4. Create classes:
# • Person → base
# • MedicalStaff(Person)
# • Doctor(MedicalStaff)
# • Surgeon(Doctor)
# Requirements:
# • Hide sensitive data (e.g., salary, patient notes)
# • Abstract method perform_duty()
# • Each level overrides the method with more specific behavior
# • Use super() to chain constructor calls
# from abc import ABC,abstractmethod
# class Person(ABC):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @abstractmethod
#     def perform_duty(self):
#         pass
# class Medicalstaff(Person):
#     def __init__(self,name,age,salary):
#         super().__init__(name,age)
#         self.__salary=salary
#     @property
#     def salary(self):
#         return self.__salary
#     def perform_duty(self):
#         return (f"{self.name} manages the hospital")
# class Doctor(Medicalstaff):
#     def __init__(self,name,age,salary,specialization):
#         super().__init__(name,age,salary)
#         self.specialization=specialization
#         self.__p_note="confidational"
#     def perform_duty(self):
#         return (f"{self.name} treat the patients from {self.specialization}")
# class Surgen(Doctor):
#     def __init__(self,name,age,salary,specialization,s_type):
#         super().__init__(name,age,salary,specialization)
#         self.s_type=s_type
#     def perform_duty(self):
#         return (f"{self.name} perfroms {self.s_type} on patient")
# p1=Medicalstaff("ammu",20,40000)
# p2=Doctor("pandu",23,70000,"neuro")
# p3=Surgen("anji",22,80000,"Neruo","brain")
# p=[p1,p2,p3]
# for per in p:
#     print(per.perform_duty())
# ammu manages the hospital
# pandu treat the patients from neuro
# anji perfroms brain on patient
# 5. Classes:
# • User
# • Instructor(User)
# • Student(User)
# • TeachingAssistant(Student, Instructor)
# Requirements:
# • Track course assignments privately
# • Ensure TAs override submit_work() and grade_work()
# • Print MRO and explain how Python resolves conflicts

# class User:
#     def __init__(self,name):
#         self.name=name
#         self.__courses=[]
#     def add_courses(self,course):
#         self.__courses.append(course)
#     def show(self):
#         return self.__courses
# class Instructor(User):
#     def grade_work(self):
#         return f"{self.name} is grading the assignments"
# class Student(Instructor):
#     def submit_work(self):
#         return f"{self.name} is submitting the assignments"
# class TeachingAssistant(Student,Instructor):
#     def grade_work(self):
#         return f"{self.name} (TA) is reviewing and grading the assigenments"
#     def submit_work(self):
#         return f"{self.name} (TA) is reviewing and submiting the assigenment"
# a=User("Ammu")
# b=Instructor("anji")
# c=Student("pandu")
# d=TeachingAssistant("sony")
# print(b.grade_work())
# print(c.submit_work())
# print(d.grade_work())
# print(d.submit_work())
# d.add_courses("python")
# print(d.show())
# 6. Create:
# • Product class with private price and quantity
# • Warehouse class containing multiple products
# • Overload:
# o + to merge warehouses
# o len() to return number of unique products
# o in operator to check if product exists
# • Provide class method to track total warehouses created
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.__price=price
        self.__quantity=quantity
    def get_quantity(self):
        return self.__quantity
    def set_quantity(self,q):
        self.__quantity=q
class Warehouse:
    total=0
    def __init__(self):
        self.products=[]
        Warehouse.total+=1
    def add_product(self,p):
        self.products[p.name] = p
    def __add__(self, other):
        new=Warehouse()
        for name in self.products:
            if name in new.products:
                old_q = new.products[name].get_quantity()
                new_q = other.products[name].get_quantity()
                new.products[name].set_quantity(old_q + new_q)
            else:
                new.products[name] = other.products[name]

            return new
    def __len__(self):
        return len(self.products)
    def __contains__(self, name):
        return name in self.products
    @classmethod
    def total_warehouses(cls):
        return cls.total
p1 = Product("Pen", 10, 5)
p2 = Product("Book", 50, 2)
p3 = Product("Pen", 10, 3)

w1 = Warehouse()
w1.add_product(p1)
w1.add_product(p2)

w2 = Warehouse()
w2.add_product(p3)

w3 = w1 + w2

print(len(w3))
print("Pen" in w3)
print(Warehouse.total_warehouses())




