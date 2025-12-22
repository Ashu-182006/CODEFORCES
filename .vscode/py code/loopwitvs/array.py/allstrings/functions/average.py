def mea(x):
    total = 0
    for i in range(len(x)):
        total += x[i]  
    avg = total / len(x)
    print(format(avg, ".6f"))
n = int(input())
a = list(map(float, input().split()))
mea(a)