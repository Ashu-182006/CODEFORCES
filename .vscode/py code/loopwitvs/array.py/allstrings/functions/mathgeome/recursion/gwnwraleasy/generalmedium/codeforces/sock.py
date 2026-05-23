a,b=map(int,input().split())
if a-b>1:
    k=(a-b)/2
    h=b
else:
    k=0
    h=a
print(h, b)
