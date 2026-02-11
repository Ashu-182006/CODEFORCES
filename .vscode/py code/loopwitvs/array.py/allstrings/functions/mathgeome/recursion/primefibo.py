def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
def is_prime(n):
    if n < 2:
        return ("not prime")
    if n == 2:
        return ("prime")
    if n % 2 == 0:
        return ("not prime")
    i = 3
    while i * i <= n:
        if n % i == 0:
            return ("not prime")
        i += 2
    return ("prime")

n = int(input())
for i in range(1, n+1):
    m=int(input())
    k=fibo(m)
    print(is_prime(k))