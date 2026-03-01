n, k = map(int, input().split())
r = set(str(i) for i in range(k + 1))

c = 0
for i in range(n):
    num = input().strip()
    d = set(num)
    if r.issubset(d):
        c += 1

print(c)