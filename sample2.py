n=int(input())
k=n//2
print(k)
for i in range(0,n):
    for j in range(1,n):
        if(j==k-i or j==k+i) or( i==0 and j==k):
             print("*",end=" ")
        else:
             print(" ",end=" ")
    print()





'''n=int(input())
for i in range(1,n):
    print(i,end=",")
print(i+1)

n=int(input())
for i in range(0,n+1):
    for j in range(1,n):
        
        if(i==j)or j==(n-i)or i==j==(n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
'''
