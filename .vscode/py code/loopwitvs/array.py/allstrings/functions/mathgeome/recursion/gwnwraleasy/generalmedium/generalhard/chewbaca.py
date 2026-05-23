x = input().strip()
result = []

for i, ch in enumerate(x):
    digit = int(ch)
    if i == 0 and digit == 9:
        result.append('9')
    else:
        result.append(str(min(digit, 9 - digit)))

print("".join(result))