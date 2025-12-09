y=[]
a=int(input())
l=-1
k=0
s=0
L=a
K=a-1
S=0
for j in range(a):
     y.append(list(map(int, input().split())))
for j in y:
    l=-1
    
    for i in j:
        
        l+=1
        if l==k:
            s+=int(i)
            k+=1
            break
k=0
for j in y:
    l=-1
    for i in j:
        
        l+=1
        if l==K:
            S+=int(i)
            K-=1
            break
print(abs(s-S))  
