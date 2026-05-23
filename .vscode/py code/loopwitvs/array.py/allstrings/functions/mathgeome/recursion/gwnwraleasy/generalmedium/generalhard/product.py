import math

N = int(input())
arr = list(map(int, input().split()))

log_sum = sum(math.log(a) for a in arr)

nth_root = math.exp(log_sum / N)
x = math.floor(nth_root) + 1
while N * math.log(x) <= log_sum + 1e-12:  
    x += 1

print(x)