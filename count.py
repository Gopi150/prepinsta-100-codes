t=f=h=c=0
amount=int(input())
while amount >100:
    if(amount>=2000):
        amount=amount%2000
        t=t+1
    elif(amount>=500):
        amount=amount%500
        f=f+1
    elif(amount>200):
        amount=amount%200
        h=h+1
    else:
        c=c+1
print(f+t+h+c)    
