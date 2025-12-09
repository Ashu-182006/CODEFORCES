while True:
    a, b = map(int, input().split())
    if a == -1 or b == -1:
        break
    start = min(a, b)
    end = max(a, b)
    numbers = list(range(start, end + 1))
    total = sum(numbers)
    print(*numbers, f"sum={total}")