import math
n=int(input())
k=n
T=0
while n>0:
    a=n%10
    n=n//10
    T=T+a**3
if(T==k):
    print(" Arm  Strong Number")
else:
    print("Not Arm Strong Number")
