n=int(input())
k=[]
sum=0
c=0
o=0
for i in range(0,n):
    a=int(input())
    k.append(a)
date=int(input())
fine=int(input())
for j in k:
    if(j%2==0):
        c=c+1
    else:
        o=o+1
if(date%2==0):
        print(o*fine)
else:
        print(c*fine)

