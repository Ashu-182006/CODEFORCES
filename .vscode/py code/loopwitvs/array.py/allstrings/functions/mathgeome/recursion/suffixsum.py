def suffix_sum(arr, n, m):
    if m == 0 or n == 0:
        return 0
    return arr[n-1] + suffix_sum(arr, n-1, m-1)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(sum(arr[n-m:]))