s = input().strip()
L = 0
R = 0
p = []
t = 0

for i in range(len(s)):
    if s[i] == 'L':
        L += 1
    else:
        R += 1
    
    if L == R:
        p.append(s[t:i+1])
        t = i + 1
        L = 0
        R = 0

print(len(p))
for k in p:
    print(k)