n = int(input())
a = input().strip()
b = list(map(int, input().split()))

t = []
for i in range(n - 1):
    if a[i] == "R" and a[i + 1] == "L":
        t.append((b[i + 1] - b[i]) // 2)

print(-1 if not t else min(t))