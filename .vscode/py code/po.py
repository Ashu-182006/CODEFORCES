t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    
    length = 1
    for i in range(n - 2, -1, -1):
        if arr[i] <= arr[i + 1]:
            length += 1
        else:
            break
    
    print(n - length)