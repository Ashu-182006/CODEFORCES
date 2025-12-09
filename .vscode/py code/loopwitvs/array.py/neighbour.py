a,b=map(int,input().split())
w=0
for i in range(1,a+1):
    y=input()
    if '.' in y:
        n=y
        w=i
c,d=map(int,input().split())
if w==c:
    m=list(n)
    if m[d-1]=='.' :
        print("yes")
    else:
        print("no")
else:
    if w==0:
        print("yes")
    else:
        print("no")