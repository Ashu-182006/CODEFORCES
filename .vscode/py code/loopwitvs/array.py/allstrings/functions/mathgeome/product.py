a,b,c=map(int,input().split())
m=1
for i in range(a,b+1):
    m=m*i%c
print(m)