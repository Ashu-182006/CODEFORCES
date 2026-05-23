n = int(input())
s = list(map(int, input().split()))
best = s[0]
worst = s[0]
k = 0
for i in range(1, n):
    if s[i] > best:    
        k += 1
        best = s[i]
    elif s[i] < worst:  
        k += 1
        worst = s[i]
print(k)
