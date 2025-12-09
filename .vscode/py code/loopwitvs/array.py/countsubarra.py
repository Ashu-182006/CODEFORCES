
x=0
x=int(input())
for i in range(x):
    m=int(input())
    y=list(map(int,input().split()))
    for i in range(len(y)):
        x+=len(y)-i
    
print(x-1)
