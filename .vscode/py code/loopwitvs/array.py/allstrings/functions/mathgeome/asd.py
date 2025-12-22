import numpy as np
r,c = map(int, input().split())
a=[]
for i in range (r):
    n = list(map(int,input().split()))
    a.append(n)
k=np.array(a)
r2,c2 = map(int, input().split())
b=[]
for i in range (r2):
    n = list(map(int,input().split()))
    b.append(n)
d=np.array(b)
if c==r2:
    f=np.dot(k,d)
    for i in f:
        print(*i)

