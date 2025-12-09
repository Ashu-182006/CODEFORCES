a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a<b and a<c:
    print(a,end=" ")
elif b>c  :
    print(c,end=" ")
else:
    print(b,end=" ")  
if a>b and a>c:
    print(a,end="")
elif b<c  :
    print(c,end="")
else:
    print(b,end="")  
