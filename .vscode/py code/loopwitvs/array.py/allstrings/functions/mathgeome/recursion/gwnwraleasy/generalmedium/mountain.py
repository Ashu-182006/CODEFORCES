a, b = map(int, input().split())
s = list(map(int, input().split()))

y = s[:]

for i in range(1, 2*a+1, 2):
    if b > 0 and y[i] - 1 > y[i-1] and y[i] - 1 > y[i+1]:
        y[i] -= 1
        b -= 1
        if b == 0:
            break

print(*y)