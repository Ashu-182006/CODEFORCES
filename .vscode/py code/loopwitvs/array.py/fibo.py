n=int(input())
a=0
i=0
b=1
k=0
c=a+b

if  n==1:
    print("0")
if n==2:
    print("1")
else:
    
    
    while i<n-2:
        a=b
        b=c
        k+=1
        if k==n-2:
            print(c,end=" ")
        c=a+b
        i+=1


