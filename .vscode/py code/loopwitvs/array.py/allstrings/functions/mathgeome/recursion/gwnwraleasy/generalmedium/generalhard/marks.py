n, m = map(int, input().split()) 
g = [input().strip() for _ in range(n)]

s = [0] * n 

for j in range(m):  
    maxi= max(g[i][j] for i in range(n))
    for i in range(n):
        if g[i][j] == maxi:
            s[i] = 1

print(sum(s))