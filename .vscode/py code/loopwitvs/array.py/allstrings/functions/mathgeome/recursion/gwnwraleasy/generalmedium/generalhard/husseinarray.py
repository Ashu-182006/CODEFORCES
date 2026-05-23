N = int(input())
A = list(map(int, input().split()))
suffixMax = [0] * N
suffixMax[-1] = A[-1]
for i in range(N-2, -1, -1):
    suffixMax[i] = max(A[i], suffixMax[i+1])
i, j = 0, 0
ans = 0
while i < N and j < N:
    if A[i] <= suffixMax[j]:
        ans = max(ans, j - i)
        j += 1
    else:
        i += 1
print(ans)