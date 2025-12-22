def shift_zeros(arr):
    o = [x for x in arr if x != 0]
    z = arr.count(0)
    r= o + [0] * z
    print(*r)

n = int(input())
arr = list(map(int, input().split()))
shift_zeros(arr)