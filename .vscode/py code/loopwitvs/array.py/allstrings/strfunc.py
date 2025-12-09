a,b=map(int,input().split())
c=list(input().strip())
for i in range(b):
    d=input().split()
    if d[0]=='pop_back':
        c.pop()
    elif d[0]=='front':
        print(c[0])
    elif d[0]=='back':
        print(c[-1])
    elif d[0]=='sort':
        c[int(d[1])-1:int(d[2])]=sorted(c[int(d[1])-1:int(d[2])])
    elif d[0]=='reverse':
        c[int(d[1])-1:int(d[2])] = c[int(d[1])-1:int(d[2])][::-1]
    elif d[0]=='print':
        print(c[int(d[1])-1])
    elif d[0]=='substr':
        print("".join(c[int(d[1])-1:int(d[2])]))
    elif d[0]=='push_back':
        c.append(d[1])
