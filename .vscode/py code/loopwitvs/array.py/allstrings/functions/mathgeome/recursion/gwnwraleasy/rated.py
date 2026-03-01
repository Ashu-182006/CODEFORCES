n = int(input())
c = False
r = []

for i in range(n):
    a, b = map(int, input().split())
    r.append(a)
    if a != b:
        c = True


if c==True:
    print("rated")
else:
   
    for i in range(n - 1):
        if r[i] < r[i + 1]:
            print("unrated")
            break
    else:
        print("maybe")