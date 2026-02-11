n=int (input())
k=j=0
for i in range (n):
    m=int(input())
    if k!=m:
        k=m
        j+=1
print(j)