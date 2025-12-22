a,b,c=map(int,input().split())
w=0
for i in range(a,b+1):
    if i%c==0:
        w+=i
print(w)