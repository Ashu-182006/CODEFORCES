def prime(a):
    if a > 1:
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                return 'NO'
        return 'YES'
    else:
        return 'NO'
b=int(input())
for i in range(1,b+1):
    a=int(input())
    print(prime(a))