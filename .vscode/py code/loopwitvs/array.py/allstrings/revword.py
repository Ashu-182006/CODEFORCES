s = input().strip()
w = s.split()
for i in range(len(w)):
    w[i]=w[i][::-1]
print(" ".join(w))