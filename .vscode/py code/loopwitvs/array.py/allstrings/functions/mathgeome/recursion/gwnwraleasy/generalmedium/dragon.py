a, b = map(int, input().split())
dragons = [tuple(map(int, input().split())) for i in range(b)]


dragons.sort()

for c, d in dragons:
    if a > c:
        a += d
    else:
        print("NO")
        break
else:
    print("YES")