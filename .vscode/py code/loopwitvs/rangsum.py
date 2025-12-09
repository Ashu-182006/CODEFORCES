

n=int(input())
for i in range(n):
    a,b =map(int,input().split())
    l=[i for i in range(a,b+1)]
    print(sum(l))