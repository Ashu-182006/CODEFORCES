n = int(input())
s = input().strip()

r= []
for i in range(n):
    if (n % 2 == 1 and i % 2 == 0) or (n % 2 == 0 and i % 2 == 1):
        r.insert(0, s[i])  
    else:
        r.append(s[i])     

print("".join(r))