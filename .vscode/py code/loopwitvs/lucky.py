x=[]
a,b=input().split()
a=int(a)
b=int(b)

for i in range(a,b+1):
    k=1
    t=i
    while t>0:
        r=t%10
        
        if r!=4 and r!=7:
            k=0
            break
        t=t//10
    if k==1:    
        x.append(i)
if len(x)==0:
    print('-1')
else:
    print(*x, sep=" ")