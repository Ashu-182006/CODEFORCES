
a,c=map(int,input().split())
y=list(map(int,input().split()))
for i in range(1,c+1):
    k=0
    for j in y:
        if i==j:
        
            k+=1
    print(k)