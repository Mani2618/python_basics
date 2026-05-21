# 1 Write a Python program using a context manager (with) to open a text file in
# read mode, read the entire content using read(), and print the number of
# characters in the file
# with open("sample.txt","r") as f:
#     f.read()
#     print(f.tell())
# 2 Write a program that opens a file using a context manager, reads all lines
# using readlines(), and prints only the lines that contain more than 10
# characters.
# with open("sample.txt","r") as f:
#     l=f.readlines()
# for i in l:
#     if len(i.strip())>10:
#         print(i.strip())
# 3 Write a program that creates a file and writes 3 lines using write(), reopens
# the same file in append mode, appends 2 more lines, and finally reads and prints
# # # the complete file content.
# with open("sample.txt","w")as f:
#     f.write("line1\n")
#     f.write("i am good girl\n")
#     f.write("i am singing\n")
# with open("sample.txt","a")as f:
#     f.write("dog braks\n")
#     f.write("dog is eating\n")
# with open("sample.txt","r") as f:
#     a=f.read()
# print(a)
# • Write a program that opens a file in read mode, reads the first 10 characters,
# prints the current cursor position using tell(), moves the cursor back to the
# # beginning using seek(0), and reads the full content again
# with open("sample.txt","r")as f:
#     d=f.read(10)
#     print(d)
#     print(f.tell())
#     f.seek(0)
#     print(f.read())
# • Create a custom context manager using a class that opens a file in write mode
# in the __enter__ method, writes a line to the file, closes the file in the
# # __exit__ method, and properly prints or logs any exception information received
# # in __exit__.
# class File:
#     def __enter__(self,):
#         self.f=open("sample.txt","w+")
#         self.f.write("hello welcome wanakam namastey")
#         return self.f
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.f.close()
# with File() as f:
#     print(f.read())
#     • Create a custom context manager using @contextmanager from the contextlib
# module that opens a file, yields the file object, and ensures the file is closed
# even if an exception occur
# from contextlib import contextmanager
# @contextmanager
# def open_file():
#     f = open("sample.txt", "w")
#     try:
#         yield f
#     finally:
#         print("File closed")
#         f.close()
# with open_file() as f:
#     f.write("Hello using contextmanager\n")
#     print(f)
# #• Write a program using a context manager that opens a file in read mode, uses a
# loop to read the file in small chunks (for example, 5 characters at a time),
# prints the cursor position after each read using tell(), uses seek() to move to
# a specific position, and continues reading from there.




