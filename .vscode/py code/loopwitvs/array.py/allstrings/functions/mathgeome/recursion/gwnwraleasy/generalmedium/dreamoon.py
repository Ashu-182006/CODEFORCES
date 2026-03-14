n, m = map(int, input().split())

k = (n + 1) // 2  
a = -1
for i in range(k, n + 1):
    if i % m == 0:
        a = i
        break

print(a)
