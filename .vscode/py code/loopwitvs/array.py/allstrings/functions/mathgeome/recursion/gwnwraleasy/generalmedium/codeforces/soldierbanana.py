k, n, w = map(int, input().split())
total = k * w * (w + 1) // 2
b = max(0, total - n)
print(b)
