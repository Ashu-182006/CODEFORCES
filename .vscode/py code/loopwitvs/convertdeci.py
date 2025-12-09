f=[]
n=int(input())
for i in range(n):
    a=int(input())
    b=bin(a)
    s=0
    j=0
    for y in b:        
        if y=='1':            
            s=s+(2**j)
            j+=1
    f.append(s)
print(*f,sep='\n')  









