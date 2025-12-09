s = input()
k = d = 0

for i in range(len(s)):
    if s[i].isalpha():
        
        if i == 0 or not s[i-1].isalpha():
            k += 1

print(k)