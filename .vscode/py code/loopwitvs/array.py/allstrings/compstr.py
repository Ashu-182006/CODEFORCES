a = input().strip()
n = len(a)

if n == 1:
    print(a)
else:
    s = None
    for i in range(1, n): 
        c = "".join(sorted(a[:i]) + sorted(a[i:]))
        if s is None or c < s:
            s = c
    print(s)