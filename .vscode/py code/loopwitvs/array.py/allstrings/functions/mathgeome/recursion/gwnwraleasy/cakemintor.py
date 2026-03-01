r, c = map(int, input().split())
k = [input().strip() for _ in range(r)]

e = 0


for i in range(r):
    if 'S' not in k[i]:
        e += c
        k[i] = '*' * c 

for j in range(c):
    if all(k[i][j] != 'S' for i in range(r)):
        for i in range(r):
            if k[i][j] == '.':  
                e += 1

print(e)