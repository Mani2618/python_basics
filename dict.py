d={"apple":100,"banana":40,"cherry":150}
s=dict(filter(lambda item:item[1]>50,d.items()))
print(s)