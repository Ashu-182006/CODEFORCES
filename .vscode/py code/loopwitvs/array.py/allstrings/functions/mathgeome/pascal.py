import math
n = int(input())

for i in range(n):
    for j in range(i + 1):
        print(math.comb(i,j), end=" ")
        
    print()