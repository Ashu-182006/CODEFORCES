x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
max_x = max(x1, x2, x3, x4)
max_y = max(y1, y2, y3, y4)
min_x = min(x1, x2, x3, x4)
min_y = min(y1, y2, y3, y4)
q = int(input())  # number of queries
for _ in range(q):
    a, b = map(int, input().split())
    if min_x <= a <= max_x and min_y <= b <= max_y:
        print("YES")
    else:
        print("NO")