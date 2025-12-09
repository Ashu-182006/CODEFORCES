a,b=input().split()
a=int(a)
b=int(b)

if a==b+1 or b==a+1 or a==b!=0:
    print("YES")
else:
    print("NO")