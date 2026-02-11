X, Y, R, N = map(int, input().split())
R2 = R * R

for _ in range(N):
    xi, yi = map(int, input().split())
    dx = xi - X
    dy = yi - Y
    if dx * dx + dy * dy <= R2:
        print("YES")
    else:
        print("NO")
