n=int(input())
k=2
for i in range(1,n+1):
    for j in range(1,i+1):
        if(j==1):
            print(k,end=" " )
            k=k+j+i
        else:
            print(k-j,end=" " )
    print()


2
3
4
