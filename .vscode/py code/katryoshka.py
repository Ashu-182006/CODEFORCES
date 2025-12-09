a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a==0 or b==0 or c==0:
    print("0")
else:
    d=min(a,b,c)
    a=a-d
    b=b-d
    c=c-d
    e=min(a//2,c)
    a=a-2*e
    c=c-e
    f=min(a//2,b,c)
    print(d+e+f)