s=input()
print(len(s))
n=int(input())
if(n%2==0):
    print("even")
else:
    print("odd")
#print(len(n))
a=0
b=1
print(a,b,end=" ")
for i in range(0,n-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
