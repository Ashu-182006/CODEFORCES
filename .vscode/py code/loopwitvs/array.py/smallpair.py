
n=int(input())
m=int(input())
d=[]
for k in range(n): 
    y=list(map(int,input().split()))
    for i in range(m):
        for j in range(i+1,m):
            e=y[i]+y[j]+j-i
            d.append(e) 
print(min(d))

