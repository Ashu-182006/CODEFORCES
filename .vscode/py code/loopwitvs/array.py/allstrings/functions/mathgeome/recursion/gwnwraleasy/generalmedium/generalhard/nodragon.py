n=int(input())
s=0
for i in range(n):
    a,b=map(int,input().split())
    if i==n-1:
        s+=a
    else:
        s+=a-b
print(s)