n=int(input())
g=0
for i in range(n):
    s=list(map(int,input().split()))
    if (s.count(0))<2:
        g+=1
print(g)