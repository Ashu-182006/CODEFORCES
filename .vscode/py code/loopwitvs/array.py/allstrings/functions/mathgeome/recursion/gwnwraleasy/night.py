s = input().strip()
c = 0  
r = 0

for ch in s:
    t = ord(ch) - ord('a')
    d = abs(t - c)
    r += min(d, 26 - d)
    c = t

print(r)