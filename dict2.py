k=[]
l=[]
n=int(input())
for i in range(0,n):
    a=input()
    k.append(a)
for i in range(0,n):
    b=input()
    l.append(b)
print(k)
print(l)
dict1={}
dict2={}
dict3=dict(zip(k,l))

for i in range(0,n):
    dict1={k[i]:l[i]}
    dict2.update(dict1)
print(dict1)
print(dict2)
print(dict3)
    
    
