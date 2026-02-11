def sum(a):
    if len(a)==0:
        return 0
    else:
        return a[0]+sum(a[1:])
n=int(input())
s=list(map(int,input().split()))
print(sum(s))