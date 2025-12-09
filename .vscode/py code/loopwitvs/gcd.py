a,b =input().split()
a=int(a)
b=int(b)
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(a)