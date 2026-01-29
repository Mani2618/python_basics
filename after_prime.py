a=int(input())
b=int(input())
res=[]
if a>b:
    step=-1
else:
    step=1
for i in range(a,b+step,step):
    if i<0:
        res.append(f"5*({i})")
    else:
        res.append(f"5*{i}")
print(", ".join(res))