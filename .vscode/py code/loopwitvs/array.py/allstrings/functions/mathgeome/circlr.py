a,b,c,d=map(int,input().split())
for i in range (d):
    m,n=map(int,input().split())
    if m>=a and n>=b:
        if m<=c and n<d:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")