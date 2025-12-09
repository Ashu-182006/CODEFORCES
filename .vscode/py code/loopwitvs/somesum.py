a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
s=0
for i in range(1,a+1):
    k=0
    
    n=i
    while n>0:
        
        r=n%10
        n=n//10
        k+=r
    if b<=k<=c:
            s+=i 
            
print(s)       