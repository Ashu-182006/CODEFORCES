n = int(input())
a = [int(input()) for _ in range(n)]
b = []
k = 0  

for x in a:
    h = x // 2
    if x % 2 != 0:  
        if k <= 0:
            h += 1
            k += 1
        else:
            k -= 1
    b.append(h)

for x in b:
    print(x)