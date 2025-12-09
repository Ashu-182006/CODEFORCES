c=[]
a,b=map(int,input().split())
for i in range(a):
    y=list(map(int,input().split()))
    c.append(list(reversed(y)))
for i in c:
    print(*i,sep=" ")
