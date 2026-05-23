n,a,b,c=map(int,input().split())
if a+b==n or a+c==n or b+c==n:
    print("2")
elif a+b+c==n:
    print("3")
    