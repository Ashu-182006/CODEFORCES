import collections
a=int(input())
s=input().strip()
c=collections.Counter(s)
if c["A"]==c["D"]:
    print("Friendship")
elif c["A"]>c["D"]:
    print("Anton")
else:
    print("Danik")