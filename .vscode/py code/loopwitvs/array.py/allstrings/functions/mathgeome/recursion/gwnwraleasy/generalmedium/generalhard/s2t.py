n=int(input())
for e in range(n):
    s=input().strip()
    t=input().strip()
    p=input().strip()
    if len(s)>len(t):
        g=sorted(t)+sorted(p)
        print(g)
        print(sorted(s))
        if set(sorted(s)). issubset(set(g)):
            print("YES")
        else:
            print("NO")
    else:
        g=sorted(s)+sorted(p)
        print(set(g))
        print(set(sorted(t)))
        if set(sorted(t)) .issubset(set(g)):
            print("YES")
        else:
            print("NO")