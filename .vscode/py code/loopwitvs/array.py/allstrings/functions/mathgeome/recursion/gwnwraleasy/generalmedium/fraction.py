import math
a, b = input().split()
a1, b1 = map(int, a.split('/'))
a2, b2 = map(int, b.split('/'))
num = math.lcm(a1 * b2, a2 * b1)
den = b1 * b2
g = math.gcd(num, den)
num //= g
den //= g
print(f"{num}/{den}")