a=[]
b =int(input())
for i in range(b):
    c,d=map(int,input().split())
    s=0
    if c<d:
        for j in range(c+1,d,):
            if j%2!=0:
                s+=j
    else:

        for j in range(d+1,c,):
            if j%2!=0:
                
                s+=j
    a.append(s)
print(*a,sep='\n')    