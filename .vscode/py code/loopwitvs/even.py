n=int(input())
if(n==0 or n==1 or n==2):
    print("-1")
for i in range(1,n+1):
    if i%2==0:
        print(i)