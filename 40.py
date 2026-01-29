a=int(input("enter a value"))
if(a<100 or a>1000):
    print("wrong")
else:
    if(a%2==0):
        print(a%3)
    else:
        print(a%2)

