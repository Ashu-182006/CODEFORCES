i=0
j=0
p=0
q,w=map(int,input().split())
y=list(map(int,input().split()))
z=list(map(int,input().split()))
while i!=len(y):
    if y[i]==z[j]:
        i+=1
        p+=1
        j+=1
    else:
        i+=1
if p==len(z):
    print("YES")
else:
    print("NO")  
