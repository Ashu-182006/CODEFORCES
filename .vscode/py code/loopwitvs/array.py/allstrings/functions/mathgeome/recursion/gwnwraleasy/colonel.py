n = int(input())
a = list(map(int, input().split()))

m = max(a)
k = min(a)

p = a.index(m)            
l = n - 1 - a[::-1].index(k) 

time = p + (n - 1 - l)
if p > l:
    time -= 1

print(time)