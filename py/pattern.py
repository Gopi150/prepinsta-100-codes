n=int(input("Enter only odd digit : "))
if (n%2==1):
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
               print("*",end=" ")
            elif(i>=n//2 and j>=n//2 ):
                print("*",end=" ")
            else:
               print(" ",end=" ")
        print()
