import math as m
n=int(input())
y=list(map(int,input().split()))
a=sum(y)
if a<0:
    x=a**2
    print(int(m.sqrt(x)))
else:
    print(a)