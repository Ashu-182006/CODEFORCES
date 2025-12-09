n = int(input())
y = list(map(int, input().split()))

k = 0


for i in range(n):
    if y[0] > 0:
        
        if i % 2 == 0 and y[i] <= 0:
            k += 1
        elif i % 2 == 1 and y[i] >= 0:
            k += 1
    else:
       
        if i % 2 == 0 and y[i] >= 0:
            k += 1
        elif i % 2 == 1 and y[i] <= 0:
            k += 1

print(k)