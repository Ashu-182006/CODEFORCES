a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())

if (c - a) * (h - f) == (d - b) * (g - e):
    print("YES")
else:
    print("NO")
