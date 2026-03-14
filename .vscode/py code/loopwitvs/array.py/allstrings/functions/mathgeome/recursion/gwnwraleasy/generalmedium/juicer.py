n, b, c = map(int, input().split())
s = list(map(int, input().split()))

g = 0
count = 0
for i in s:
    if i <= b:
        g += i
        if g > c:
            count += 1
            g = 0
print(count)