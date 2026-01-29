n=int(input())
step=1
num=2
sum=0
for i in range(n+1):
    if num>n:
         break
    sum+=num
    avg=sum/step
    print(avg)
    num=num+(step+1) * 2
    step+=1




                   