a,b=map(int,input().split())
s=list(map(int,input().split()))
d=0
for i in s:
    
    if int(i)>=s[b-1] and int(i)>0:
        d+=1
print(d)