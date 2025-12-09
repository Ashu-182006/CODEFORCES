a = []
n = int(input()) 
for i in range(n):
    x = int(input())
    f= 1
    for j in range(1, x + 1):
        f*= j
    a.append(f)
for b in a:
    print(b)