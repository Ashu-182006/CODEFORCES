def noofways(n, m):
    for i in range(1, m):
        if n+i==m:
            return i**2
n, m = map(int, input().split())
print(noofways(n, m))
