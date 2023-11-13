n=int(input())
s=0
c=0
k=n
for i in range(1,n):
    
    if(s<n):
        s=s+i
        print(i,end=" ")
        
        if(s==n):
                s=0
                c=c+1
                print(c)
    
        
    
    
print()        
print(c)
print(s)
        
        
        
