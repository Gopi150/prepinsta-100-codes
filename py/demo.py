'''n=int(input("No of Number :"))
targrt=int(input("Enter Your Target Value :"))
arr=[]
out=[]
for i in range(n):
      arr.append(int(input()))
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==targrt:
            out.append([i,j])
if len(out)==0:
    #print("[]")
    print("False")
else:
    #print(out)
    print("True")'''
a=5
if a>=1 or a<=9:
    print("yes")

        
        
