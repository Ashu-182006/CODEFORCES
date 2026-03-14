n=int(input())
k=0
for i in range (1,n+1):
    if i%2!=0:
        k-=i
    else:
        k+=i
print(k)