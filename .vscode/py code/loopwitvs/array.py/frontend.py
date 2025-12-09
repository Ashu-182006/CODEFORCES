a=[]
n=int(input())
y=list(map(int,input().split()))
i=0
j=n-1
k=0
while i!=n:
   if i ==0 or i%2==0:
        a.append(y[k])
        i+=1
        k+=1
   else:
       a.append(y[j])
       j-=1
       i+=1
print(*a,sep=" ")     