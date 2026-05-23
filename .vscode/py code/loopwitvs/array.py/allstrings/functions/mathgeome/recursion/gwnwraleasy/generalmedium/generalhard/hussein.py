a=input().strip()
b=input().strip()
if len(a) != len(b):
    print("NO")
else:
    diff = [i for i in range(len(a)) if a[i] != b[i]]
    
    if len(diff) == 0:
        print("YES")
    elif len(diff) == 2:
        i, j = diff[0], diff[1]
        a = list(a)
        a[i], a[j] = a[j], a[i]
        print("YES" if a == list(b) else "NO")
    else:
        print("NO")