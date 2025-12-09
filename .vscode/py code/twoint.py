a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=((a*b*c*d)%100)
if e<10:
    print("0{}".format(e))
else:
    print(e)