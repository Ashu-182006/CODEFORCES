n, m, k = map(int, input().split())
cnt3 = min(n, m, k)
n -= cnt3
m -= cnt3
k -= cnt3
cnt2 = min(n // 2, m, k)
n -= cnt2 * 2
m -= cnt2
k -= cnt2
cnt1 = min(n // 2, k)

print(cnt1 + cnt2 + cnt3)