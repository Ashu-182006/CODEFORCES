n = int(input())
a = list(map(int, input().split()))
s, d = 0, 0
l, r = 0, n - 1
t = 0  

while l <= r:
    if a[l] >= a[r]:
        p = a[l]
        l += 1
    else:
        p = a[r]
        r -= 1

    if t == 0:
        s += p
    else:
        d += p

    t^= 1  
 
print(s, d)