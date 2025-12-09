a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if(a>=c and b<=d and a<=b):
    print("{} {}".format(a,b))
elif(a>=c and b>=d and a<=d):
    print("{} {}".format(a,d))
elif(a<=c and b<=d and c<=b):
    print("{} {}".format(c,b))
elif(a<=c and b>=d and c<=d):
    print("{} {}".format(c,d))
else:
    print("-1")