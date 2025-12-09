import math as m
a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if((b*m.log(a))>(d*m.log(c))):
    print("YES")
else:
    print("NO")