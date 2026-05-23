a=list(map(int,input().strip()))
b=list(map(int,input().strip()))
c=[]
for i,j in zip(a,b):
    if i==j:
        c.append('0')
    else:
        c.append('1')
print("".join(c))