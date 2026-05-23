import collections
a=input().strip()
b=input().strip()
c=input().strip()
d=a+b
if collections.Counter(c) ==collections.Counter(d):
    print("YES")
else:
    print("NO")
