b=[]
x=int(input())
for i in range(x):
    m=int(input())
    y=list(map(int,input().split()))
    a=[]
    for i in range(len(y)):
        for j in range(i,len(y)):
     
            a.append((y[i:j+1]))
    
    
    v=0
    for u in a:
        
        if all(u[j]<u[j+1] for j in range(len(u)-1)):
            v+=1
        
            
    b.append(v)
print(*b,sep="\n")  
    

    
