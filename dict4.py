n=int(input())
d1={}
c=0
y=0
for i in range(1,n+1):
            a=input("key:")
            b=int(input("value:"))
            c=c+b
            d={a:b}
            d1.update(d)
            s=d1[a]
            y=s+y
print(d1)
print(c)
print(y)

