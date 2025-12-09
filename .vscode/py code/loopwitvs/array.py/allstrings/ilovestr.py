n=int(input())
c=[]
for j in range(n):
    a,b=input().split()
    i=0
    s=""
    while i!=max(len(a),len(b)):
        if i<len(a):
            s+=a[i]
        if i<len(b)  :  
            s+=b[i]
        i+=1
    c.append(s)
print(*c,sep="\n")
