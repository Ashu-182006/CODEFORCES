n = int(input())
b = "ROYGBIV"
e = "GBIV"
r = b
n -= 7
r += (e * (n // 4)) + e[:n % 4]
print(r)