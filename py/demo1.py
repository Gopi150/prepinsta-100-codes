n=input()
a=[]
for i in n:
    if i in a :
        a.remove(i)
    else:
        a.append(i)
           
print(a)
        
