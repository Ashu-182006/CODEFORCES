n=int(input())
y=list(map(int,input().split()))
print(min(y),end=" ")
print(y.index(min(y))+1)