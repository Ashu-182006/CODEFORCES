a,b = map(int,input().split())
s = list(map(int,input().split()))
s.sort()

ans = min(s[i+a-1] - s[i] for i in range(b-a+1))
print(ans)