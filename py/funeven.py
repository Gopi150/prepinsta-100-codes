'''def even(n):
    if n%2==0:
        print(n,end="")#2,
        '''
def add(a):
    sum=sum+a

n=int(input())
sum=0
for i in range(1,n+1):                  #intial,end,step
    #even(i)
    add(i)
print(sum)
