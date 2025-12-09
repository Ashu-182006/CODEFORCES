n=int(input())
y=list(map(int,input().split()))
for i in y:
    if i==min(y):
        s=i
    elif i==max(y):
        b=i

for i in y:
    if i==min(y):
        i=b
    elif i==max(y):
        i=s
    print(i,end=" ")
