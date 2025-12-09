n=int(input())
k=0
y=list(map(int,input().split()))
for i in y:
    if (int(i)+1) in y:
        k+=1
print(k)