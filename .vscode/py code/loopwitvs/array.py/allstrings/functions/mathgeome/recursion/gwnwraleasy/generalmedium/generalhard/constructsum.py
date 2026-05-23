T = int(input())
for _ in range(T):
    n, s = map(int, input().split())
    total = n * (n + 1) // 2
    if s > total:
        print(-1)
        continue
    
    ans = []
    for i in range(n, 0, -1):
        if s >= i:
            ans.append(i)
            s -= i
        if s == 0:
            break
    
    if s == 0:
        print(len(ans), *ans)
    else:
        print(-1)