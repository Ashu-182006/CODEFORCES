def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a, b = map(int, input().split())

if isprime(b):
    for i in range(a+1, b):
        if isprime(i):
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")