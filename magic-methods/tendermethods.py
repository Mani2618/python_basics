# class ReverseString:
#     def __init__(self, text):
#         self.text = text
#         self.index = len(text) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= 0:
#             char = self.text[self.index]
#             self.index -= 1
#             return char
#         else:
#             raise StopIteration
#
#
# for ch in ReverseString("Python"):
#     print(ch)
# class MyEnumerate:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.data):
#             result = (self.index, self.data[self.index])
#             self.index += 1
#             return result
#         else:
#             raise StopIteration
#
#
# lst = ["a", "b", "c"]
# for i in MyEnumerate(lst):
#     print(i)
class Num:
    def __init__(self,n):
        self.n=n
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.n:
            value=self.current
            self.current+=1
            return value
        else:
            raise StopIteration
obj=Num(9)
for i in obj:
    print(i)
# class Even:
#     def __init__(self,data):
#         self.data=data
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<len(self.data):
#             value=self.data[self.index]
#             self.index+=1
#             if value%2==0:
#                 return value
#         raise StopIteration
# nums=[1,2,3,45,6,7,8,9]
# for i in Even(nums):
#     print(i)
# def digit(n):
#     for d in str(n):
#         yield int(d)
# for s in digit(1234):
#     print(s)
# 6def sum(list):
#     total=0
#     for i in list:
#         total+=i
#         yield total
# for j in sum([1,2,3]):
#     print(j)
# def vowel(text):
#     vowels="aeiouAEIOU"
#     for i in text:
#         if i in vowels:
#             yield i
# for v in vowel("Mani"):
#     print(v)
#
# class Word:
#     def __init__(self,s):
#         self.words=s.split()
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.words):
#             n=self.words[self.index]
#             self.index+=1
#             return n
#         else:
#             raise StopIteration
# for a in Word("this is iterator"):
#     print(a)


# class Even:
#     def __init__(self,text):
#         self.text=text
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if  self.index<len(self.text):
#             char=self.text[self.index]
#             self.index+=2
#             return char
#         else:
#             raise StopIteration
# for ch in Even("python"):
#     print(ch)
# def max(lst):
#     maximum=lst[0]
#     for i in lst[0:]:
#         if i>maximum:
#             maximum=i
#         yield maximum
# for j in max([3,1,4,2]):
#     print(j)
