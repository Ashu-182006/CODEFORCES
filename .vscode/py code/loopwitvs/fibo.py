n=int(input())

a=0
i=0
b=1
if n>=1:
    print(a,end=" ")
else: 
    print()
if n>=2:

    print(b,end=" ")
c=a+b
while i<n-2:
    a=b
    b=c
    print(c,end=" ")
    c=a+b
    i+=1


