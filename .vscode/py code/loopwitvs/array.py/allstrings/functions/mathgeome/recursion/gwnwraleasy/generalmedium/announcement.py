n = int(input().strip())
l = list(map(int, input().split()))

d = len(set(l))

if d == n:
    print(-1)
else:
    print(n - d)