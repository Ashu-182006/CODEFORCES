def log2(a):
    if a == 1:
        return 0
    return 1 + log2(a // 2)

a = int(input())
print(log2(a))