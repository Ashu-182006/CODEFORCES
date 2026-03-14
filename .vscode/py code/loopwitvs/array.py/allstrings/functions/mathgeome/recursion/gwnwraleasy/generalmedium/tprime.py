def is_prime(num):
    if num <= 1:
        return False
    s = 0
    for i in range(2, int(num) + 1):
        if num % i == 0:
            s+=1
            if s>2:

                return False
    if s==2:
        return True
    return False
n=int(input())
a=list(map(int,input().split()))
for i in a:
    if is_prime(i):
        print("YES")
    else:
        print("NO")