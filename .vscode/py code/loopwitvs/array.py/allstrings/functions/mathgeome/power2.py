def powertwo(n):
    if n > 0 and (n & (n - 1)) == 0:
        return "YES"
    else:
        return "NO"
n = int(input())
print(powertwo(n))