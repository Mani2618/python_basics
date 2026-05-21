# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(end="* ")
#     print()
# r=int(input())
# c=int(input())
# for i in range(1,r+1):
#     for j in range(1,c+1):
#         print(end="* ")
#     print()
# r=int(input())
# c=int(input())
# for i in range(1,r+1):
#     for j in range(1,c+1):
#         print(i,end=" ")
#     print()
# r=int(input())
# c=int(input())
# for i in range(1,r+1):
#     for j in range(1,c+1):
#         print(j,end=" ")
#     print()
# r=int(input())
# c=int(input())
# for i in range(1,r+1):
#     for j in range(1,c+1):
#         print(f"{i}{j}",end=" ")
#     print()
# n=int(input())
# #
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(end="1 ")
#     print()
# n=int(input())
#
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print(end="1 ")
#         elif i<=j:
#             print(end="2 ")
#         else:
#             print(end="0 ")
#     print()
#
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j>=n+1:
#             print(1,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# n=int(input())
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if i>=j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#
#     print()
# @
#
# # #
#
# @ @ @
#
# # # # # #
#
# @ @ @ @ @
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             if i%2==0:
#                 print("#",end=" ")
#             else:
#                 print("@",end=" ")
#     print()
# op
# @
# # #
# @ @ @
# # # # #
# @ @ @ @ @

#
# n = int(input())
# b = 1
# if n <= 0:
#     print("Invalid Input")
# else:
#     for i in range(n, 0, -1):
#         if b % 2 == 1:
#             for j in range(1, i + 1):
#                 print(j, end=" ")
#         else:
#             c = i
#             for j in range(1, i + 1):
#                 print(c, end=" ")
#                 c -= 1
#         print()
#         b += 1
#
#
# 1 2 3 4 5
# 4 3 2 1
# 1 2 3
# 2 1
# 1
# n=int(input())
# b=1
# for i in range(n,0,-1):
#     if b%2==1:
#         for j in range(1,i+1):
#             print(j,end=" ")
#     else:
#         c=i
#         for j in range(1,i+1):
#             print(c,end=" ")
#             c-=1
#     print()
#     b+=1

# n=int(input())
#
# if n>=10:
#     for i in range(1,n+1):
#         print("  "*(n-i),end="")
#         for j in range(i):
#             if i>=10:
#                 print(f"{i}  ",end="")
#             else:
#                 print(f" {i}  ",end="")
#         print()
#     for i in range(n-1,0,-1):
#         print("  "*(n-i),end="")
#         for j in range(i):
#             if i>=10:
#                 print(f"{i}  ",end="")
#             else:
#                 print(f" {i}  ",end="")
#         print()n=int(input())
# # for i in range(1,n+1):
# #     c=64+n
# #     for j in range(1,n+1):
# #         if j<=n-i:
# #             print("  ",end="")
# #         else:
# #             print(chr(c),end=" ")
# #             c-=1
# #     print()
# else:
#     for i in range(1,n+1):
#         print(" "*(n-i),end="")
#         for j in range(1,i+1):
#             print(i,end=" ")
#         print()
#     for i in range(n-1,0,-1):
#         print(" "*(n-i),end="")
#         for j in range(1,i+1):
#             print(i,end="")
#         print()
#
#
#
# n=int(input())
# a=1
# for i in range(1,n+1):
#     print("   "*(n-i),end="")
#     for j in range(1,i+1):
#         print(f"{a:02d} ",end="")
#         a+=1
#     print()
# n=int(input())
# p=[]
# s=2
# while len(p)<n:
#     for i in range(2,int(s**0.5)+1):
#         if s%i==0:
#             break
#     else:
#         p.append(s)
#     s+=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(p[j],end="")
#     print()
# n=int(input())
# for i in range(1,n+1):
#     b=i
#     c=n-1
#     for j in range(1,i+1):
#         print(b,end=" ")
#         b+=c
#         c-=1
#     print()
# a=int(input())
# for i in range(1,a+1):
#     b=i
#     c=a-1
#     for j in range(1,i+1):
#         print(b,end="")
#         b+=c
#         c-=1
#     print()
