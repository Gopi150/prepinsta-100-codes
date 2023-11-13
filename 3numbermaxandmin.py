a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c and b>c):
    print("max = a")
    print("min =c")
elif(c>b and c>a and b>a):
    print("max = c")
    print("min = a")
else:
    if(c>a):
      print("max = b")
      print("min =a")
    else:
      print("max = b")
      print("min = c")
    
    


    

