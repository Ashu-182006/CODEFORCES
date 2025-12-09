n=int(input())
i=-1
k=0
y=list(map(int,input().split()))
while i!=-3:
    i+=1
    if y[i]%2==0:
        y[i]=y[i]//2
        
        if i==len(y)-1:
            i=-1
            k+=1
    else:
        break
print(k)
    
                