d=[]
a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    if b==c:
        d.append("Square")
    else:
        d.append("Rectangle")
print(*d,sep="\n")