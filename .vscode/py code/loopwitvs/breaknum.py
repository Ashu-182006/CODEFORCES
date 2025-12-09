b=[]

n=int(input())
c=list(map(int,input().split()))
for y in c:
    k=0
    
    h=int(y)
    while h%2==0:
        k+=1
        h=h//2
    b.append(k)    

print(max(b))