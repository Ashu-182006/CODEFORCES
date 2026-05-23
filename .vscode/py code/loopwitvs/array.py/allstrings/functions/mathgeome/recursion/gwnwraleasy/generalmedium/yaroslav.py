n = int(input())
s = list(map(int, input().split()))

freq = {}
for x in s:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

max_freq = max(freq.values())

if max_freq <= (n + 1) // 2:
    print("YES")
else:
    print("NO")