n=int(input())
b=list(map(int, input().split()))
c=-1
d=max(b)
e=l=min(b)
for i in b:
    c+=1
    if i==d:
        d=c
    if i==e:
        e=c
if d>e:
    print(d+(n-1-e)-2)
else:
    print(d+(n-1-e))