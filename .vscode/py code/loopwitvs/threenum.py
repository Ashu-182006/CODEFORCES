a,b=map(int,input().split())
k=0
g=[]
for i in range(a+1):
    for j in range(a+1):
        for k in range(a+1):
            if i+j+k==b:
                g.append(b)
                
print(len(g))