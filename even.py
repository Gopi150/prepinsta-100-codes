def sum(n):
    if(n==1 or n==0):
        return 0
    elif(n%2==0):
        return n+sum(n-2)
    else:
        return (n-1)+sum(n-2)
                         


                         
n=int(input())
print(sum(n))
