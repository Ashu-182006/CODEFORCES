n = int(input())
a = list(map(int, input().split()))
a.sort()
d=0
for i in range(n-2):
    if a[i] + a[i+1] > a[i+2]:
        d+=1
        print("YES")
        break

if d == 0:
    print("NO")
