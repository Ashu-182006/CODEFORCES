a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
if (d-b)*(e-c)==(f-d)*(c-a):
    print("YES")
else:
    print("NO")