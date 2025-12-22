import math
x = int(input())
if x <= 1:
    print("NO")
else:
    p = True
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            p = False
            break
    print("YES" if p else "NO")