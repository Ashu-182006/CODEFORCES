a=list(map(int,input().split()))
a.sort()
k=a[1]-a[0]+a[2]-a[1]
print(k)