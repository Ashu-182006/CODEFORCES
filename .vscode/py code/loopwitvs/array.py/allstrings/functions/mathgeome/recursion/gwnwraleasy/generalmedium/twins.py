n = int(input())
c= list(map(int, input().split()))
c.sort(reverse=True)
total = sum(c)
m = 0
t = 0
for coin in c:
    m += coin
    t += 1
    if m > total - m:
        break
print(t)