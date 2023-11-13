s=input()
c=0
n=s
for i in n:
    if n[0:]!=s[:-1]:
        print(n[0:])
        print(s[:-1])
        c=c+1
print(c-5)
