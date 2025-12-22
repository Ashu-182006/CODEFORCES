a,b,c=map(int,input().split())
d=1
for i in range(a,b+1):
        d=(d*i)%c
print(d)