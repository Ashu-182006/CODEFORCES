def maxim(a):
    print("The maximum number :", max(a))

def minim(a):
    print("The minimum number :", min(a))

def prime(a):
    t = 0
    for i in a:
        if i > 1:  # 1 is not prime
            is_prime = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                t += 1
    print("The number of prime numbers :", t)

def palin(a):
    t = 0
    for i in a:
        if str(i) == str(i)[::-1]:
            t += 1
    print("The number of palindrome numbers :", t)

def divisor(a):
    maxa = 0
    xin = 0
    for i in a:
        ma = 0
        for j in range(1, i + 1):
            if i % j == 0:
                ma += 1
        if ma > maxa or (ma == maxa and i > xin):
            maxa = ma
            xin = i
    print("The number that has the maximum number of divisors :", xin)

# Main
x = int(input())
a = list(map(int, input().split()))
maxim(a)
minim(a)
prime(a)
palin(a)
divisor(a)