n=int(input())
y=list(map(int,input().split()))
s=min(y)
k=0
for i in y:
    if i==s:
        k+=1
if k%2==0:
    print("Unlucky")
else:
    print("Lucky")