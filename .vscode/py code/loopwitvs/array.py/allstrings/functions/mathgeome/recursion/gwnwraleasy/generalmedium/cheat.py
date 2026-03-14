n = int(input())
if n == 0:
    print(1)  
else:
    cycle = [8, 4, 2, 6]
    print(cycle[(n-1) % 4])