# #1
# class Animal:
#     def sound(self):
#         print("animals make sounds")
# class Dog(Animal):
#     def sound(self):
#         print("dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("cat meow")
# class Cow(Animal):
#     def sound(self):
#         print("Cow ambha")
#
# animals=[Dog(),Cat(),Cow()]
# for i in animals:
#     i.sound()
# # 2
# class Car:
#     def start(self):
#         print("car started")
# class Computer:
#     def start(self):
#         print("Computer started")
# class Washingmachine:
#     def start(self):
#         print("Washing has been started")
# def operate(device):
#     device.start()
# operate(Car())
# operate(Computer())
# operate(Washingmachine())

# 3
# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return Vector(self.x+other.x,self.y+other.y)
#     def __eq__(self,other):
#         return self.x==other.x,self.y==other.y
#     def __str__(self):
#         return f"({self.x},{self.y})"
# v1=Vector(2,3)
# v2=Vector(2,3)
# v3=v1+v2
# print(v3)
# print(v1==v2)

# 4
# class Transport:
#     def move(self):
#         print("Transport is moving")
# class Bus(Transport):
#     def move(self):
#         super().move()
#         print("bus moves on road")
# class Bike(Transport):
#     def move(self):
#         super().move()
#         print("bike is moving")
# b=Bus()
# b.move()
# bk=Bike()
# bk.move()


# 6
# class Payment:
#     def process(self,amount):
#         print("processing payment to you ",amount)
# class CreditCardPayment(Payment):
#     def process(self,amount,card_type="sbi"):
#         print("processing",amount,"using",card_type)
# p=Payment()
# p.process(900)
# c=CreditCardPayment()
# c.process(200)
# 7
# class Sorter:
#     def __init__(self,strategy):
#         self.strategy=strategy
#     def change(self,strategy):
#         self.strategy=strategy
#
#     def sort(self,data):
#         return self.strategy.sort(data)
# class BS:
#     def sort(self,data):
#         print("bubble sort")
#         return sorted(data)
# class MS:
#     def sort(self,data):
#         print("merge sort")
#         return sorted(data)
# class QS:
#     def sort(self,data):
#         print("Quick sort")
#         return sorted(data)
#
# data=[5,7,8,9]
# s=Sorter(BS())
# print(s.sort(data))

# 8

# class Account:
#     def withdraw(self,amount):
#         print(f"withdrawing {amount} from account")
# class Savings(Account):
#     def withdraw(self,amount):
#         print("checking savings")
#         print(f"withdrawing {amount} from savings")
# class PremiumSavings(Account):
#     def withdraw(self,amount):
#         super().withdraw(amount)
#         print("applied permium services")
# a=Account()
# s=Savings()
# p=PremiumSavings()
# types=[a,s,p]
# for a in types:
#     print("---")
#     a.withdraw(2000)

#9
# class Cricle:
#     def draw(self):
#         print("Drawing Circle")
# class Square:
#     def draw(self):
#         print("Drawing square")
# class Rectangle:
#     def draw(self):
#         print("rectangle")
# class Car:
#     def draw(self):
#         print("Car")
# def draw(shape):
#     shape.draw()
# a=[Cricle(),Square(),Rectangle(),Car()]
# for i in a:
#     draw(i)

# 10
#
# class Payment:
#     def pay(self, amount):
#         raise NotImplementedError("Subclasses must implement pay()")
# class UPI(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using UPI.")
# class Card(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using Card.")
# class Cash(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using Cash.")
# def process_payment(payment_method, amount):
#     payment_method.pay(amount)
# p1 = UPI()
# p2 = Card()
# p3 = Cash()
# process_payment(p1, 500)
# process_payment(p2, 1000)
# process_payment(p3, 200)

