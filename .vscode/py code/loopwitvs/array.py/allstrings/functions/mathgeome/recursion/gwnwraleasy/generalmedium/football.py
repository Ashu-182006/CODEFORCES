n = int(input())
s = [input().strip() for i in range(n)]

from collections import Counter
c = Counter(s)

print(max(c, key=c.get))
