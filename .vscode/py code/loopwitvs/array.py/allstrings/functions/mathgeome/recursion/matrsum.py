def sumOftwomatrices(A, B):
    n = len(A)
    m = len(A[0])
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result
A = []
B = []
n, m = map(int, input().split())
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)
for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)
result = sumOftwomatrices(A, B)
for row in result:
    print(' '.join(map(str, row)))
    