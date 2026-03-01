n=int(input())
a=list(map(int, input().split()))
b=0
d=0
for i in a:
    if i>0:
        b+=i
    elif i<0 and b>0:
        b-=1    
    else:
        d+=1
print(d)