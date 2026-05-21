def prime(a,b):
    res=[]
    for i in range(a,b+1):
        fc=0
        for j in range(1,i+1):
            if i %j==0:
                fc+=1
        if fc==2:
            res.append(i)
    return sum(res[::2])
a=int(input())
b=int(input())
print(prime(a,b))
