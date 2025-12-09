import collections as x
a = input()

b = x.Counter(a)
for char in sorted(b):  
    print(char, ":", b[char])