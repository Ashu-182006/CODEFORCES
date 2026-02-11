def base(x):
    s=bin(x)
    print(s[2::])
n=int(input())
for i in range(n):
    s=int(input())
    base(s)
