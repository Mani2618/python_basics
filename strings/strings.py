#1
# s="python"
# print(len(s))
# 2
# s="python"
# for i in s:
#     print(ord(i))
# 3
# s="python"
# print(s.upper())
# 4
# s="PYTHON"
# print(s.lower())
# 5
# s="mani is"
# print(s.replace(" ","-"))
# 6
# s="123456"
# print(s.isdigit())
# 7
# s="adsdfghj"
# print(s.isalpha())
# 8
# s="Ammu123"
# print(s.isalnum())
# 9
# s=input()
# c=0
# if len(s)==12:
#     for i in range(0,len(s)):
#         if s[i]>"0" and s[i]<="9":
#             c=c+1
#         else:
#             print("Invalid")
#     if c==len(s):
#         print("valid")
#     else:
#         print("Invalid")
# #10

# 11
# s="manaswithaellanki@gmail.com"

# 12
# s="Ammu@2005"
# uc = lc = dc = sc = space = 0
# for ch in s:
#     if ch.isupper():
#         uc += 1
#     elif ch.islower():
#         lc += 1
#     elif ch.isdigit():
#         dc += 1
#     elif ch == " ":
#         space += 1
#     else:
#         sc += 1
# if len(s) >= 8 and uc > 0 and lc > 0 and dc > 0 and space == 0:
#     print("Valid Password")
# else:
#     print("Invalid Password")
#
#     if len(s) < 8:
#         print("- Minimum 8 characters required")
#     if uc == 0:
#         print("- At least one uppercase letter required")
#     if lc == 0:
#         print("- At least one lowercase letter required")
#     if dc == 0:
#         print("- At least one digit required")
#     if space > 0:
#         print("- Spaces are not allowed")
# s=input()
# print(s[::-1])
#
# s=input()
# print(s.reverse())
# converting the string (reverse) with out predefined function by using list
# s=input()
# l=0
# r=len(s)-1
# sl=list(s)
# while l<=r:
#     sl[l],sl[r]=sl[r],sl[l]
#     l+=1
#     r-=1
# print(str(sl))
# s=input()
# s1=s[::-1]
# if s==s1:
#     print("palindrome")
# else:
#     print("not")
# s=input()
# l=s.split()
# for i in range(0,len(s)):
#     print(l[i][::-1],end=" ")

