n = int(input())
t = list(map(int, input().split()))
p, m, y = [], [], []
for i in range(n):
    if t[i] == 1:
        p.append(i+1)
    elif t[i] == 2:
        m.append(i+1)
    else:
        y.append(i+1)
w = min(len(p), len(m), len(y))
print(w)
for i in range(w):
    print(p[i], m[i], y[i])