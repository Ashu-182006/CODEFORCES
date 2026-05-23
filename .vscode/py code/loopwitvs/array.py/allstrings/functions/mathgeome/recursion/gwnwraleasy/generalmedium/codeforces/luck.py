n=int(input())
for i in range (n):
    k=input().strip()
    if sum(int(i) for i in k[:3])==sum(int(i) for i in k[3:]):
        print("YES")
    else:
        print("NO")