def combination(n, r, memo={}):
    if (n, r) in memo:
        return memo[(n, r)]
    if r == 0 or r == n:
        memo[(n, r)] = 1
    else:
        memo[(n, r)] = combination(n-1, r-1, memo) + combination(n-1, r, memo)
    return memo[(n, r)]

n, r = map(int, input().split())
print(combination(n, r))