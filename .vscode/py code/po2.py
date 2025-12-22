import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    ones = [i for i, ch in enumerate(s) if ch == '1']
    
    if len(ones) == n:
        print(0)
        continue
    
    max_gap = 0
    for i in range(len(ones)):
        j = (i + 1) % len(ones)
        gap = (ones[j] - ones[i] - 1) % n
        max_gap = max(max_gap, gap)
    
    print(max_gap)