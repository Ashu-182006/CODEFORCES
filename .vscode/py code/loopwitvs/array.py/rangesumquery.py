e=[]
a,b=map(int,input().split())
y=list(map(int,input().split()))
s=0
for i in range(b):
    c,d=map(int,input().split())
    for j in range(c-1,d):
        s+=y[j]
    e.append(s)    
    s=0
print(*e,sep="\n")