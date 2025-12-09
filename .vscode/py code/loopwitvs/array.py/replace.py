n=int(input())
k=-1
y=list(map(int,input().split()))
for e in y:
    k+=1
    if e>0:
        y[k]=1
    elif e<0:
        y[k]=2
    else:
        y[k]=0
print(*y,sep=" ")