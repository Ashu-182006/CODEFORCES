b=[]
n=int(input())
for i in range(n):
    o=0
    e=0
    a=int(input())
    y=list(map(int,input().split()))
    if a%2!=0:
        b.append(-1)
    else:
        for i in y:
            if (int(i))%2==0:
                e+=1
            else:
                o+=1
        if e==o:
            b.append(0)
        else:
            b.append(int((max(o,e)-min(o,e))/2))
print(*b,sep="\n")
