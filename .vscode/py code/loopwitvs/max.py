n = int(input())
y = list(map(int, input().split()))
m=y[0]
for i in y:
    if i>m:
        m=i
print(m)