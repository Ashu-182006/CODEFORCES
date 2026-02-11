a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
k=0
r=[]
for i in b:
    k+=i
    r.append(k)
for i in d:
    for j in r:
        k+=1
        if i<j:
            print(k)
            break
