def leftmax(a, n=0):
    if n == len(a) - 1:   
        return a[n]
    return max(a[n], leftmax(a, n+1))

n = int(input())
a = list(map(int, input().split()))
print(leftmax(a))