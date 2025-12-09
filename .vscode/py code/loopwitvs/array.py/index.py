n=int(input())
y=list(map(int,input().split()))
m=int(input())
p=0
k=-1
for e in y:
    k+=1
    if e==m:
        p=1
        break
if p==1:
    print(k)
else:
    print("-1")