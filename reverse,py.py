n=int(input())
rev=0
while n>0:
    a=n%10
    n=n//10
    rev=rev*10+a
print(rev)
    
    
