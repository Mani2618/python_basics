def alter(a,b):
    fc=0
    res=[]
    for i in range(a,b+1):
        fc=0
        for j in range(1,i+1):
            if i %j==0:
                fc+=1
        if fc==2:
            res.append(i)
    return res[::2]
a=int(input())
b=int(input())
print(alter(a,b))


