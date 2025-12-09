a,b=map(int,input().split())
k=[]
i=0
p=0
s=0
c=int((bin(a)[2:]))
d=int((bin(b)[2:]))
e= c+d
for y in str(e):
    if y=='2':
        k.append('0')
    else:
        k.append(y)
t=int(''.join(map(str,k)))
while t>0:
    r=t%10
    t=t//10    
    if r==1:
        s+=(2**p)
    p+=1    
print(s)        
