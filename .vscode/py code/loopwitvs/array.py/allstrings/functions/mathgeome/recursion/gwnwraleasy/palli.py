s = list(input().strip())
n = len(s)

for i in range(n // 2):
    j = n - 1 - i
    if s[i] == s[j] == '?':
        s[i] = s[j] = 'a'
    elif s[i] == '?':
        s[i] = s[j]
    elif s[j] == '?':
        s[j] = s[i]
    elif s[i] != s[j]:
        print(-1)
        break
else:
    if n % 2 == 1 and s[n // 2] == '?':
        s[n // 2] = 'a'
    print(''.join(s))