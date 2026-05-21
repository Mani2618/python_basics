# class InsufficientBalance(Exception):
#     pass
# class BankAccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         if amount<0:
#             raise InsufficientBalance("amount can't be negitive")
#         else:
#             self.balance-=amount
# a=BankAccount(10000)
# try:
#     a.withdraw(-5)
# except InsufficientBalance as e:
#     print("Error:",e)

# class Book:
#     def __init__(self):
#         self.title=input()
#         self.author=input()
#         self.price=int(input())
#         if self.price < 0:
#             raise ValueError("price cant be negitive")
#     def display_details(self):
#         return self.title,self.author,self.price
# try:
#     b=Book()
#     b.display_details()
# except ValueError as e:
#     print("Error:",e)


# from abc import ABC,abstractmethod
# class UserBase(ABC):
#     @abstractmethod
#     def get_role(self):
#         pass
# class Member(UserBase):
#     count=0
#     admin_flag=0
#     def __init__(self,name,credentials):
#         self.name=name
#         self._credentials=credentials
#         self.__perms=[]
#     def add(self,perm):
#         self.__perms+=perm
#     def sub(self,perm):
#         if perm in self.__perms:
#             self.__perms-=perm
#     def __eq__(self, other):
#         if other==self.__perms:
#             print("both are equall")
#     @classmethod
#     def a(cls,new=2,new2=4):
#         cls.admin_flag=new
#         cls.count=new2
#     def __str__(self):
#         return self._credentials
#     def __repr__(self):
#         return self._credentials
#
#     def get_role(self):
#         print("its working")
# m=Member("mani","12345676")
# m.add("oil")
# m.add("salt")
# m.sub("salt")
# m.get_role()


