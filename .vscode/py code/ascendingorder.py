a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if(a>=b) and (a>=c) and (b>=c):
    print(c)
    print(b)
    print(a)
elif(a>=b) and (a>=c) and (c>=b):
    print(b)
    print(c)
    print(a)
elif(b>=a) and (b>=c) and (a>=c):
    print(c)
    print(a)
    print(b)
elif(b>=a) and (b>=c) and (c>=a):
    print(a)
    print(c)
    print(b)
elif(c>=a) and (c>=b) and (a>=b):
    print(b)
    print(a)
    print(c)
elif(c>=a) and (c>=b) and (b>=a):
    print(a)
    print(b)
    print(c)

print()
print(a)
print(b)
print(c)

