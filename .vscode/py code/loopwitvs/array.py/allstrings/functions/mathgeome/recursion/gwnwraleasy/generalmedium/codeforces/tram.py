n=int(input())
k=0
m=0
for i in range (n):
    a,b=map(int,input().split())
    k-=a
    k+=b
    m=max(m,k)
print(m)