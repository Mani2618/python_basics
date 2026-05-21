#1
# n=list(map(int,input().split()))
# print(n)
# 2
# n=list(map(int,input().split()))
# n.insert(3,40)
# print(n)
# [3, 40]
#3
# l=list(map(int,input().split()))
# l1=list(map(int,input().split()))
# l.extend(l1)
# print(l)
# [10, 20, 30, 20, 30, 40]
#4
# n=list(map(int,input().split()))
# i=int(input())
# if i in n:
#     n.remove(i)
#     print(n)
# else:
#     print("not ")
# 10 30 40 6
# 6
# [10, 30, 40]
# 5
# n=list(map(int,input().split()))
# i=int(input())
# if i in n:
#     n.pop(i)
#     print(n)
# else:
#     print("not")
# 1 2 3 4
# 3
# [1, 2, 3]

#6
# n=list(map(int,input().split()))
# s=int(input())
# l=n.index(s)
# print(l)
# 1 12 3 4 5
# 12
# 1

#7
# n=list(map(int,input().split()))
# a=n.count(10)
# print(a)
# 10 20 10 20 10 30
# 3

#8
# n=list(map(int,input().split()))
# b=n[0]
# c=n[-1]
# a=b+c
# print(a)
# 1 2 3 4
# 5


#9
# Write a program to calculate the sum of list elements up to a given index
# n=list(map(int,input().split()))
# a=4
# sum=0
# for i in range(a+1):
#     sum+=n[i]
# print(sum)
# 1 2 3 4 5
# 15

# Write a program to calculate the average of odd numbers in a list.
# n=list(map(int,input().split()))
# a=4
# sum=0
# avg=0
# c=0
# for i in range(a+1):
#     if i%2==1:
#         sum+=n[i]
#         c+=1
# avg=sum/c
# print(avg)

# Write a program to print the list in reverse order
# n=list(map(int,input().split()))
# n.reverse()
# print(n)
# Write a program to print all prime numbers present in a list
# n=list(map(int,input().split()))
#
# for i in n:
#     c=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             c=False
#             break
#     if c:
#         print(i,end=" ")

#next prime from the list

# l=list(map(int,input().split()))
# for num in l:
#     n=num+1
#     while True:
#         c=True
#
#         for j in range(2,int(n**0.5)+1):
#             if n%j==0:
#                 c=False
#                 break
#         if c:
#             print(n,end=" ")
#         n+=1

#14
# l=list(map(int,input().split()))
# k=int(input())
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if (l[i] + l[j]==k):
#             print(f"{l[i],l[j]}")

# practice
# l=list(map(int,input().split()))
# k=int(input())
# if k in l:
#     for i in range(l.count(k)):
#         l.remove(k)
#     print(*l)
# 1 2 1 3 4 1
# 1
# 2 3 4



# string slicing
# a=list(map(int,input().split()))
# # print(a[1:3])
# # print(a[0:4])
# # print(a[5:3:1])
# # print(a[5:3:-1])
# print(a[-5:4:1])
# liner serch
# a=list(map(int,input().split()))
# k=int(input())
# b=False
# for i in range(len(a)):
#     if (k==a[i]):
#         b=True
#         break
# if b:
#     print("Found")
# else:
#     print("Not")
# #binary search
# a=list(map(int,input().split()))
# k=int(input())
# l=0
# r=len(a)-1
# a.sort()
# b=False
# while l<=r:
#     m=(l+r)//2
#     if a[m]==k:
#         b=True
#         break
#     elif k>a[m]:
#         l=m+1
#     else:
#         r=m-1
# if b:
#     print("s")
# else:
#     print("no")
# l=list(map(int,input().split()))
# m=min(l)
# for i in range(m,0,-1):
#     c=0
#     for j in range(len(l)):
#         if l[j]%i==0:
#             c=c+1
#     if c==len(l):
#         print(i)
#         break

# l=list(map(int,input().split()))
# m=max(l)
# k=m
# while True:
#     c=0
#     for i in range(len(l)):
#         if m%l[i]==0:
#             c=c+1
#     if c==len(l):
#         print(m)
#         break
#     m=m+k
# l=list(map(int,input().split()))
# m=min(l)
# for i in range(m,0,-1):
#     c=0
#     for j in range(len(l)):
#         if l[j]%i==0:
#             c=c+1
#     if c==len(l):
#         print(i)
#         break
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     c=l.count(l[i])
#     print(f"{l[i]}+{c}")
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     c=0
#     for j in range(len(l)):
#         if l[i]==l[j]:
#             c=c+1
#     print(f"{l[i]}+{c}")
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     c=0
#     for j in range(len(l)):
#         if l[j]%l[i]==0:
#             c=c+1
#     if c==1:
#         print(l[i])
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     c=0
#     for j in range(len(l)):
#         if l[j]%l[i]==0:
#             c=c+1
#     if c==1:
#         print(l[i])
# l=list(map(int,input().split()))
# h1=float("-inf")
# h2=h1
# h3=h2
# for i in range(len(l)):
#     if l[i]>h1:
#         h3=h2
#         h2=h1
#         h1=l[i]
#
#     elif l[i]>h2:
#         h3=h2
#         h2=l[i]
#     elif l[i]>h3:
#         h3=l[i]
# print(h3)
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# l=list(map(int,input().split()))
# n=int(input())
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l[len(l)-n])
