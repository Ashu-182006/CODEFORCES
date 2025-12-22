import math as m
a,b,c=map(int,input().split())
if a+b>c and b+c>a and a+c>b:
    print("Valid")
    s=(a+b+c)/2
    d=(s*(s-a)*(s-b)*(s-c))
    print(m.sqrt(d))
else:
    print("Invalid")
