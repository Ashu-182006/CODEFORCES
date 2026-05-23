n, k = map(int, input().split())
letters = [chr(ord('a') + i) for i in range(k)]
password = []
for i in range(n):
    password.append(letters[i % k])
for i in range(1, n):
    if password[i] == password[i-1]:
        password[i] = letters[(i+1) % k]
print("".join(password))