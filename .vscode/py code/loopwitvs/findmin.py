a, b = map(int, input().split())
c = list(map(int, input().split()))
d = []

for i in range(0, len(c), b):
    e= c[i:i+b]
    d.append(min(e))

print(*d,sep=" ")