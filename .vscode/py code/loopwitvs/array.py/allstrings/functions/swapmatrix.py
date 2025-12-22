def matrix(m,a,b,c):
    m[b-1],m[c-1]=m[c-1],m[b-1]
    for i in m:
        i[b-1],i[c-1]=i[c-1],i[b-1]
    for i in m:
        for j in i:
            print(j,end=' ')
        print()            
m=[]
a,b,c=map(int,input().split())
for i in range(a):
    m.append(list(map(int,input().split())))
matrix(m,a,b,c)