n=int (input())
k=0
for i in range (n):
    a,b=map(int,input().split())
    if a+2<=b:
        k+=1
print(k)
        