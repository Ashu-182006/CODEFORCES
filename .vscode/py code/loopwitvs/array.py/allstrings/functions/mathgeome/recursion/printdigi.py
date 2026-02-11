def digit(x):
    if x == 0:
        print(0, end=" ")
        return
    if x < 10:
        print(x, end=" ")
        return
    digit(x // 10)
    print(x % 10, end=" ")
t = int(input())
for i in range(t):
    a = int(input())
    digit(a)
    print()  