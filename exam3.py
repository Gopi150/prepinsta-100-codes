n=int(input())
k=[]
sum=0
for i in range(0,n):
    a=int(input())
    k.append(a)
for i in range(0,n,2):
    sum=sum+k[i]
print(sum)
