n, t = map(int, input().split())
if n == 1 and t == 10:
    print(-1)
else:
    num = 10**(n-1)
    if num % t != 0:
        num += t - (num % t)
    print(num)