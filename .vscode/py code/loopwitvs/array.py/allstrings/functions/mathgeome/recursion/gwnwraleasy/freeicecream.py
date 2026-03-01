a,b = map(int, input().split())
t=0
for i in range(a):
    c,d=map(str, input().split())
    if c=="+":
        b+=int(d)
    else:
        b-=int(d)
        
    if b<0:
        t+=1
        b+=int(d)
print(b,t)