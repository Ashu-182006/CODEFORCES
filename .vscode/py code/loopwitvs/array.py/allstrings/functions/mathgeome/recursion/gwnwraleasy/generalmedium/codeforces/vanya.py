a,b=map(int,input().split())
c=list(map(int,input().split()))
k=0
for i in c:
    if int (i)>b:
        k+=2
    else:
        k+=1
print(k)