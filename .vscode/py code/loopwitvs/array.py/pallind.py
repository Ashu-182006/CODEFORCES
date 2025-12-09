n=int(input())
y=list(map(int,input().split()))
b= list(reversed(y))

if y==b:
    print("YES")
else:
    print("NO")
