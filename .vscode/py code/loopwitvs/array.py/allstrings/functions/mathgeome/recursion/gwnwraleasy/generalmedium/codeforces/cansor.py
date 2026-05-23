def cansort(n, k, arr):
    if k == 1:
        return arr == sorted(arr)
    else:
        return True
t = int(input().strip())
for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print("YES" if cansort(n, k, arr) else "NO")
