def solve():
    k = int(input())
    nums = list(map(int, input().split()))
    chosen = []
    if 0 in nums:
        chosen.append(0)
    for x in nums:
        if 1 <= x <= 9:
            chosen.append(x)
            break
    for p in [10, 100]:
        if p in nums:
            chosen.append(p)
    if not chosen:
        chosen.append(nums[0])
    print(len(chosen))
    print(*chosen)
if __name__ == "__main__":
    solve()
 