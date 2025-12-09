a = input().strip()
i = 0
j = 0
target = "hello"

while i < len(a) and j < len(target):
    if a[i] == target[j]:
        j += 1
    i += 1

if j == len(target):
    print("YES")
else:
    print("NO")