a,b=map(int,input().split())
s=o=e=0
for i in range(min(a,b),max(a,b)+1):
    s+=i
    if i%2==0:
        e+=i
    else:
        o+=i
print(s)
print(e)
print(o)