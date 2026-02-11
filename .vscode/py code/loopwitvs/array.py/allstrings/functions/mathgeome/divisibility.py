a, b, x = map(int, input().split())
if a > b:
    a, b = b, a
l = ((a + x - 1) // x) * x
r = (b // x) * x
if l > r:
    print(0)
else:
    n = (r - l) // x + 1
    result = n * (l + r) // 2
    print(result)