n=int(input())
l=[]
s=[]
for i in range(1,n+1):
    a=(i)
    l.append(a)
    b=(i*i)
    s.append(b)
d={x:x*x for x in range(1,n+1)}
'''a=input()
    l.append(a)
    b=input()
    s.append(b)
    '''
dict3=dict(zip(l,s))
print(dict3)
print(d)
'''
keys=a
value=1
'''
