n, m = map(int, input().split())

for row in range(n):
    a = list(input().strip())
    k = []
    for col in range(m):
        if a[col] == "-":
            k.append("-")
        elif (row + col) % 2 == 0:
            k.append("B")
        else:
            k.append("W")
    print("".join(k))