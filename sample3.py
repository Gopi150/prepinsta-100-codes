n=int(input())
k=n//2
for i in range(0,n+1):
    for j in range(1,n):
        
        if(i==(n-1)and j==k) or (i==j and j==k):
            print("*",end=" ")
        elif(i==1 and(j==0 or j==1 or j==3 or j==4) or  i==2 and(j==0 or j==4)or i==3 and(j==0 or j==1 or j==3) or (i==2 and j==0)):
             print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
