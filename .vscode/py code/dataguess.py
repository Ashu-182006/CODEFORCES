a,b,c=map(int,input().split())
d=((a*b)/c)
p=int(d)
if d!=p:
    print("double")
elif d==p:
    if -2147483648 <= d <=2147483647   :
        print("int")
    else:
        print("long long") 
