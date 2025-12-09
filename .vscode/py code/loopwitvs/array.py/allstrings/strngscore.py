n = int(input())
s = 0
i = 0
l = list(input().strip())

while i < len(l):
    if l[i] == 'V':
        s += 5
        i += 1
    elif l[i] == 'W':
        s += 2
        i += 1
    elif l[i] == 'X':
        if i + 1 < len(l):
            l.pop(i + 1)  
        i += 1
    elif l[i] == 'Z':
        if i + 1 < len(l):
            if l[i + 1] == 'V':
                s //= 5
                l.pop(i + 1) 
            elif l[i + 1] == 'W':
                s //= 2
                l.pop(i + 1) 
        i += 1
    elif l[i] == 'Y':
        if i + 1 < len(l):
            l.append(l.pop(i + 1))
        i += 1
    else:
        i += 1

print(s)