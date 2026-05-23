n, k = map(int, input().split())
a= 240 - k

t = 0
s = 0

for i in range(1, n + 1):
    if t + 5 * i <= a:
        t += 5 * i
        s += 1
    else:
        break

print(s)
