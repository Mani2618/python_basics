from functools  import reduce
n=[1,3,7,8,4]
l1=reduce(lambda a,b: a if a>b else b ,n)
print(l1)