import collections
a=int(input())
c=collections.Counter(str(a))
if c['4']+c['7']==4 or c['4']+c['7']==7:
    print("YES")
else:
    print("NO")