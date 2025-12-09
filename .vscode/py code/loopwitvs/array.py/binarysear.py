d=[]
a,b=map(int,input().split())
y=list(map(int,input().split()))
for i in range(b):
    c=int(input())
    if c in y:
        d.append("found")
    else:
        d.append("not found")
print(*d,sep="\n")