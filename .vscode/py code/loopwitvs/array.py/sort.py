n=int(input())
y=list(map(int,input().split()))

j=0
while j!= len(y)-1:
    i=0
    while i!=len(y)-1:
        if y[i+1]<y[i]:
            t=y[i]
            y[i]=y[i+1]
            y[i+1]=t
        i+=1 
    j+=1
print(*y,sep=" ")

    