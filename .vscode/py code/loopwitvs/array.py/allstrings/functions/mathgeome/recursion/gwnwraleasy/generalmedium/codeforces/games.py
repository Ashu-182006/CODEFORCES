from itertools import count
n = int(input())
t = [tuple(map(int, input().split())) for i in range(n)]
c = 0
for i in range(n):
    for j in range(n):
        if i != j and t[i][0] == t[j][1]:
            c += 1
print(c)
