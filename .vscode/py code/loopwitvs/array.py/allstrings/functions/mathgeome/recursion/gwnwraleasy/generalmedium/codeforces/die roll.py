import math
Y, W = map(int, input().split())
M = max(Y, W)
num = 6 - M + 1
den = 6
g = math.gcd(num, den)
print(f"{num//g}/{den//g}")
